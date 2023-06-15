#standard library imports
from collections import OrderedDict
from copy import *

#local application imports
from .Item import *
from Gramática.GLC import GLC




class SLR:
    def __init__(self,grammar):
        self.grammar = grammar
        self.srlGrammar = self.enumerateGrammar(grammar)  #lista del formato (numero,noTerminal,produccion)
        self.listItems = []
        self.actualItem = 0
        self.listGoto = []  #lista del formato (partida,simbolo,llegada)
        self.table = {}

    def buildCollection(self):
        initialGrammar = GLC(self.grammar.initial + "'")
        initialGrammar.add_production(self.grammar.initial + "'", ". "+self.grammar.initial)
        item = Item(str(self.actualItem), self.grammar, initialGrammar)
        item.closing([])
        self.listItems.append(item)
        self.actualItem += 1

        for item in self.listItems:
            elements = item.elements()
            for element in elements:
                self.movePoint(element,item)

    def movePoint(self,element,itemP):
         auxGrammar = GLC("X")
         itemSGrammar = itemP.grammar.productions
         control = False    #para controlar cuando crear una nueva gramática
         for noTerminal in itemSGrammar:
            list = itemSGrammar[noTerminal]
            for prod in list:
                elementList = prod.split()
                tam = len(elementList)
                for index, letter in enumerate(elementList):
                    if letter == "." and index != tam - 1:  #Si el punto no está al final
                        if elementList[index + 1] == element:
                            aux = copy(elementList)
                            aux[index], aux[index+1] = aux[index+1], aux[index]
                            newProduction = ' '.join(aux)
                            if control == False:
                                auxGrammar.initial = noTerminal
                                control = True
                            auxGrammar.add_production(noTerminal,newProduction)   
         c, name = self.exist(auxGrammar)
         if c == False:
             item = Item(str(self.actualItem),self.grammar,auxGrammar)
             item.closing([])
             self.listItems.append(item)
             self.listGoto.append((itemP.name,element,self.actualItem))
             self.actualItem += 1
         else:
            self.listGoto.append((itemP.name,element,name))

    def exist(self, grammar):        
        for item in self.listItems:
            if self.compareGrammars(grammar,item.nonClosingGrammar):
                return True,item.name
        return False,""

    def compareGrammars(self,g1, g2):
            grammar1 = g1.productions
            grammar2 = g2.productions
            if len(grammar1) != len(grammar2):
                return False
    
            for key in grammar1:
                if key not in grammar2 or grammar1[key] != grammar2[key]:
                    return False
    
            return True     
    
    def enumerateGrammar(self, grammar):
        aux = []
        i = 1
        for nonTerminal in self.grammar.productions:
            list = self.grammar.productions[nonTerminal]
            for prod in list:
                aux.append((i,nonTerminal,prod))
                i += 1
        return aux

    def printItems(self):
        for item in self.listItems:
            print(item.name)
            item.grammar.print_productions()

    def printGoto(self):
        for element in self.listGoto:
            print(element)

    def initializeTable(self):
        for i in range(self.actualItem):
            self.table[str(i)] = {}
            for element in self.grammar.terminals:
                (self.table[str(i)])[element] = None
            self.table[str(i)]["$"] = None
            for element in self.grammar.nonTerminals:
                (self.table[str(i)])[element] = None

    def defineAccept(self):
        aux = GLC(self.grammar.initial + "'")
        aux.add_production(self.grammar.initial + "'",self.grammar.initial+" .")
        for item in self.listItems:
            if (self.grammar.initial + "'") in item.nonClosingGrammar.productions:
                if aux.productions[self.grammar.initial + "'"][0] in item.nonClosingGrammar.productions[self.grammar.initial + "'"]:
                    (self.table[item.name])["$"] = "ACC"
                    break

    def buildTable(self):
        self.buildCollection()
        self.initializeTable()
        self.defineAccept()
        for element in self.listGoto:
            start,symbol,end = element
            if symbol in self.grammar.terminals:
                if (self.table[start])[symbol] == None:
                    (self.table[start])[symbol] = "S" + str(end)
                else:
                    print("------------------------")
                    print("Error en la gramática, no es una válida para este análisis")
                    print("------------------------")
                    self.table = {}
                    return
            else:
                if (self.table[start])[symbol] == None:
                    (self.table[start])[symbol] = (str(end))
                else:
                    print("------------------------")
                    print("Error en la gramática, no es una válida para este análisis")
                    print("------------------------")
                    self.table = {}
                    return
        self.grammar.get_first()
        followingS = self.grammar.get_following()
        self.fillReduceTable(followingS)

    def identifyFinishedProductions(self,item,followingS):
        grammar = item.grammar
        for nonTerminal in grammar.productions:
            list = grammar.productions[nonTerminal]
            for prod in list:
                if prod[-1] == '.':
                    for element in self.srlGrammar:
                        number,nT,p = element  #número, no terminal y produccion
                        if prod[:-2] == p and nonTerminal == nT:
                            print("R" + str(number) + " en los siguientes de " + nT + " en I" + str(item.name))
                            for symbol in followingS[nT]:
                                if (self.table[item.name])[symbol] == None:
                                    (self.table[item.name])[symbol] = "R"+str(number)
                                else:
                                    #print("TABLA")
                                    #print(self.table[item.name])
                                    #print("SIGUIENTES")
                                    #print(self.grammar.followingS[nT])
                                    #print("R" + str(number) + " en los siguientes de " + nT + " en I" + str(item.name))
                                    print("------------------------")
                                    #print("Error en la gramática, no es una válida para este análisis")
                                    print("Conflicto al armar la tabla, se tomará la primera opción")
                                    print("------------------------")
                                    #self.table = {}
                                    #return
                        
    def fillReduceTable(self,followingS):
        for item in self.listItems:
            self.identifyFinishedProductions(item,followingS)
            if self.table == {}:
                return

    def printTable(self):
        print("TABLE")
        for item,dic in self.table.items():
            aux = ""
            for key,element in dic.items():
                aux += ("[" + key + "]" + ":" + str(element) + "  ")
            print(str(item) + " -> " + aux)

    def analyze(self, instruction):
        if self.table != {}:
            input = instruction.split()
            for word in input:
                if word not in self.grammar.terminals:
                    print("------------------------")
                    print("Error de sintaxis: La palabra " + word + " no pertenece al lenguaje.")
                    print("------------------------")
                    return
            print("------------------------")
            print("ANÁLISIS")
            print("------------------------")
            input.append("$")
            stack = ["0"]
            control = True
            while control == True:
                print("STACK: " + str(stack))
                print("INPUT: " + str(input))
                res = (self.table[stack[-1]])[input[0]]
                if res == None: 
                    aux = []
                    print("------------------------")
                    print("Entrada: " + instruction)
                    print("Error de sintaxis en la palabra " + input[0]+ ".")
                    for key, value in self.table[stack[-1]].items():
                        if value != None and key in self.grammar.terminals: 
                            aux.append(key)
                    print("Se puede usar " + " ó ".join(aux) + " en su lugar.")
                    print("------------------------")
                    return
                if res[0] == 'S': #SHIFT
                    print("SHIFT")
                    stack.append(input[0])
                    del input[0]
                    aux = (self.table[stack[-2]])[stack[-1]]
                    aux = aux[1:]
                    stack.append(aux)
                    print("------------------------")
                elif res[0] == 'R': #REDUCE BY
                    n,nt,p = self.srlGrammar[int(res[1:])-1]
                    print("REDUCE BY: " + nt + " -> " + p)
                    numberToReduce = len(p.split()) * 2
                    for i in range (numberToReduce):
                        stack.pop()
                    stack.append(nt)
                    aux = (self.table[stack[-2]])[stack[-1]]
                    stack.append(aux)
                    print("------------------------")
                elif res == "ACC":
                    print("------------------------")
                    print("Entrada: " + instruction)
                    print("Instrucción válida!")
                    print("------------------------")
                    control = False
