from ItemCLR import *
from GrammarCLR import *
from GLC import *
from copy import *

class CLR:
    def __init__(self,grammar):
        self.grammar = grammar
        self.crlGrammar = self.enumerateGrammar(grammar)  #lista del formato (numero,noTerminal,produccion)
        self.listItems = []
        self.actualItem = 0
        self.listGoto = []  #lista del formato (partida,simbolo,llegada)
        self.table = {}
        self.firstS = grammar.get_first()

    def buildCollection(self):
        initialGrammar = GrammarCRL(self.grammar.initial + "'")
        initialGrammar.add_production(self.grammar.initial + "'", (". "+self.grammar.initial,["$"]))
        item = ItemCLR(str(self.actualItem), self.grammar, self.firstS, initialGrammar)
        item.closing([])
        self.listItems.append(item)
        self.actualItem += 1

        for item in self.listItems:
            elements = item.elements()
            for element in elements:
                self.movePoint(element,item)

    def movePoint(self,element,itemP):
         auxGrammar = GrammarCRL("X")
         itemSGrammar = itemP.grammar.productions
         control = False    #para controlar cuando crear una nueva gramática
         for noTerminal in itemSGrammar:
            list = itemSGrammar[noTerminal]
            for prod in list:
                elementList = prod[0].split()
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
                            auxGrammar.add_production(noTerminal,(newProduction,prod[1]))   

         c, name = self.exist(auxGrammar)
         if c == False:
             item = ItemCLR(str(self.actualItem),self.grammar,self.firstS,auxGrammar)
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
        aux = GrammarCRL(self.grammar.initial + "'")
        aux.add_production(self.grammar.initial + "'",(self.grammar.initial+" .",["$"]))
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
        self.fillReduceTable()
        
    def fillReduceTable(self):
        for item in self.listItems:
            self.identifyFinishedProductions(item)
            if self.table == {}:
                return
            
    def identifyFinishedProductions(self,item):
        grammar = item.grammar
        for nonTerminal in grammar.productions:
            list = grammar.productions[nonTerminal]
            for prod in list:
                if (prod[0])[-1] == '.':
                    for element in self.crlGrammar:
                        number,nT,p = element
                        if (prod[0])[:-2] == p:
                            for symbol in prod[1]:
                                if (self.table[item.name])[symbol] == None:
                                    (self.table[item.name])[symbol] = "R"+str(number)
                                else:
                                    #print("TABLA")
                                    #print(self.table[item.name])
                                    #print("SÍMBOLOS DE ANTICIPACIÓN")
                                    #print(prod[1])
                                    #print("R" + str(number) + " en " + ", ".join(prod[1]) + " en I" + str(item.name))
                                    print("------------------------")
                                    #print("Error en la gramática, no es una válida para este análisis")
                                    print("Conflicto al armar la tabla, se tomará la primera opción")
                                    print("------------------------")
                                    #self.table = {}
                                    #return
        
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
                #print("STACK: " + str(stack))
                #print("INPUT: " + str(input))
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
                    #print("SHIFT")
                    stack.append(input[0])
                    del input[0]
                    aux = (self.table[stack[-2]])[stack[-1]]
                    aux = aux[1:]
                    stack.append(aux)
                    #print("------------------------")
                elif res[0] == 'R': #REDUCE BY
                    n,nt,p = self.crlGrammar[int(res[1:])-1]
                    #print("REDUCE BY: " + nt + " -> " + p)
                    numberToReduce = len(p.split()) * 2
                    for i in range (numberToReduce):
                        stack.pop()
                    stack.append(nt)
                    aux = (self.table[stack[-2]])[stack[-1]]
                    stack.append(aux)
                    #print("------------------------")
                elif res == "ACC":
                    print("------------------------")
                    print("Entrada: " + instruction)
                    print("Instrucción válida!")
                    print("------------------------")
                    control = False

'''
grammar = GLC("S")
grammar.add_production("S","C C")
grammar.add_production("C","c C")
grammar.add_production("C","d")
grammar.print_productions()
'''
'''
grammar = GLC("S")
grammar.add_production("S","L = R")
grammar.add_production("S","R")
grammar.add_production("L","* R")
grammar.add_production("L","id")
grammar.add_production("R","L")
grammar.print_productions()
'''
'''
grammar = GLC("S")
grammar.add_production("S","A A")
grammar.add_production("A","a A")
grammar.add_production("A","b")
grammar.print_productions()
'''
'''
grammar = GLC("Programa")
print("------------------------")
print("NUESTRA GRAMÁTICA")
print("------------------------")
grammar.add_production("Programa","🜉 \\n ListaSentencia \\n 🝓")    
grammar.add_production("Type","🝰")   
grammar.add_production("Type","🝯") 
grammar.add_production("Type","🝮") 
grammar.add_production("ReturnType","Type") 
grammar.add_production("ReturnType","🜸")   
grammar.add_production("IdentificadorVariable","🝳 nombre 🝳")
grammar.add_production("IdentificadorFuncion","🜛 nombre ☾ Argumentos ☽ 🜛")   
grammar.add_production("Declaracion","Type _ IdentificadorVariable")  
grammar.add_production("Asignar","IdentificadorVariable _ 🝑 _ Expresion") 
grammar.add_production("Expresion","ExpresionAritmetica")  
grammar.add_production("Expresion","ExpresionBooleana")
grammar.add_production("OperandoAritmetico","IdentificadorVariable") 
grammar.add_production("OperandoAritmetico","numero")
grammar.add_production("OperadorComparacion","🜔")     
grammar.add_production("OperadorComparacion","🜕")
grammar.add_production("OperadorComparacion","🜖")
grammar.add_production("OperadorComparacion","🜗")
grammar.add_production("OperadorComparacion","🜎")
grammar.add_production("OperadorComparacion","🜍")
grammar.add_production("OperandoBooleano","vera")  
grammar.add_production("OperandoBooleano","malvera")
grammar.add_production("OperandoBooleano","IdentificadorVariable")
grammar.add_production("IfCondition","se _ ☾ ExpresionBooleana ☽ \\n 🜚 \\n ListaSentencia \\n 🜚 ElseCondition") 
grammar.add_production("ElseCondition","\\n alie \\n 🜚 \\n ListaSentencia \\n 🜚") 
grammar.add_production("ElseCondition","λ")
grammar.add_production("WhileLoop","dum _ ☾ ExpresionBooleana ☽ \\n 🜚 \\n ListaSentenciaCiclo \\n 🜚")  
grammar.add_production("ListaSentenciaCiclo","ListaSentencia")
grammar.add_production("ListaSentenciaCiclo","ListaSentencia \\n ListaSentenciaCiclo")
grammar.add_production("ListaSentenciaCiclo","rompi")
grammar.add_production("ListaSentenciaFuncion","ListaSentencia") 
grammar.add_production("ListaSentenciaFuncion","ListaSentencia \\n ListaSentenciaFuncion")
grammar.add_production("ListaSentenciaFuncion","reveni IdentificadorVariable")
grammar.add_production("Comparacion","OperandoAritmetico _ OperadorComparacion _ OperandoAritmetico") 
grammar.add_production("ListaSentencia","Sentencia")
grammar.add_production("ListaSentencia","Sentencia \\n ListaSentencia")
grammar.add_production("Sentencia","Declaracion")
grammar.add_production("Sentencia","Expresion")
grammar.add_production("Sentencia","WhileLoop")
grammar.add_production("Sentencia","IfCondition")
grammar.add_production("Sentencia","\\n")
grammar.add_production("Sentencia","Comentarios")
grammar.add_production("ExpresionAritmetica","ExpresionAritmetica _ 🜂 _ Termino")
grammar.add_production("ExpresionAritmetica","ExpresionAritmetica _ 🜄 _ Termino")   
grammar.add_production("ExpresionAritmetica","Termino")
grammar.add_production("Termino","Termino _ 🜁 _ Factor") 
grammar.add_production("Termino","Termino _ 🜃 _ Factor")
grammar.add_production("Termino","Factor")
grammar.add_production("Factor","☾ ExpresionAritmetica ☽")  
grammar.add_production("Factor","OperandoAritmetico") 
grammar.add_production("ExpresionBooleana","ExpresionBooleana _ 🝘 _ TerminoBool") 
grammar.add_production("ExpresionBooleana","TerminoBool")
grammar.add_production("ExpresionBooleana","Comparacion")
grammar.add_production("TerminoBool","TerminoBool _ 🜓 _ FactorBool")
grammar.add_production("TerminoBool","FactorBool")
grammar.add_production("FactorBool","🝱 FactorBool")
grammar.add_production("FactorBool","☾ ExpresionBooleana ☽")
grammar.add_production("FactorBool","OperandoBooleano")
grammar.add_production("Funcion","funkcio _ ReturnType _ IdentificadorFuncion ☾ Argumentos ☽ \\n 🜚 \\n ListaSentenciaFuncion \\n 🜚") 
grammar.add_production("Argumentos","Declaracion") 
grammar.add_production("Argumentos","Declaracion , Argumentos")
grammar.add_production("Argumentos","λ")
grammar.add_production("Comentarios","ComentarioSimple")  
grammar.add_production("Comentarios","ComentarioBloque")
grammar.add_production("ComentarioSimple","🜌 Sentencia")  
grammar.add_production("ComentarioSimple","🜌 rompi")
grammar.add_production("ComentarioSimple","🜌 reveni")
grammar.add_production("ComentarioBloque","🜋 ListaSentenciaFuncion 🜋") 
grammar.add_production("ComentarioBloque","🜋 ListaSentenciaCiclo 🜋")
'''
'''
grammar = GLC("AritmetikaEsprimo")
print("------------------------")
print("NUESTRA GRAMÁTICA")
print("------------------------")
grammar.add_production("BukloDum","dum Komparo Ordonoj finiDum")
grammar.add_production("Komparo","Operatoro KondicoOpe Operatoro")
grammar.add_production("Operatoro","Identigilo")
grammar.add_production("Operatoro","Nombroj")
grammar.add_production("Ordonoj","Ordo ;")
grammar.add_production("Ordonoj","Ordo ; Ordonoj")
grammar.add_production("Ordo","Kondico")
grammar.add_production("Ordo","BukloDum")
grammar.add_production("Ordo","Asigni")
grammar.add_production("Kondico","se ( Komparo ) Ordonoj fini")
grammar.add_production("Kondico","se ( Komparo ) Ordonoj alie Ordonoj")
grammar.add_production("KondicoOpe","=")
grammar.add_production("KondicoOpe",">=")
grammar.add_production("KondicoOpe","<=")
grammar.add_production("KondicoOpe","<>")
grammar.add_production("KondicoOpe","<")
grammar.add_production("KondicoOpe",">")
grammar.add_production("Identigilo","litero")
grammar.add_production("Identigilo","litero RestoDeLiteroi")
grammar.add_production("Nombroj","NombroEntjero")
grammar.add_production("Nombroj","NombroReala")
grammar.add_production("NombroEntjero","nombro")
grammar.add_production("NombroEntjero","nombro NombroEntjero")
grammar.add_production("NombroReala","NombroEntjero . NombroEntjero")
grammar.add_production("Asigni","Identigilo := AritmetikaEsprimo")
grammar.add_production("RestoDeLiteroi","literoN")
grammar.add_production("RestoDeLiteroi","literoN RestoDeLiteroi")
grammar.add_production("AritmetikaEsprimo","( AritmetikaEsprimo AritOperatoro AritmetikaEsprimo )")
grammar.add_production("AritmetikaEsprimo","Identigilo")
grammar.add_production("AritmetikaEsprimo","Nombroj")
grammar.add_production("AritmetikaEsprimo","AritmetikaEsprimo AritOperatoro ) AritmetikaEsprimo")
grammar.add_production("AritOperatoro","+")
grammar.add_production("AritOperatoro","*")
grammar.add_production("AritOperatoro","-")
grammar.add_production("AritOperatoro","/")

#grammar.firstPhase()
#grammar.second_phase()
#grammar.left_factoring()
#grammar4.eliminate_indirect_left_recursion()
#grammar.eliminate_left_recursion()
#grammar.print_productions()

grammar.print_productions()
'''

grammar = GLC("Program")
grammar.add_production("Program", "Statement")
grammar.add_production("Program", "Statement Program")
grammar.add_production("Statement", "Assignment")
grammar.add_production("Statement", "IfStatement")
grammar.add_production("Statement", "WhileLoop")
grammar.add_production("Statement", "ForLoop")   #
grammar.add_production("Assignment", "identifier = Expression ;")
grammar.add_production("IfStatement", "if ( Condition ) { Program }")
grammar.add_production("IfStatement", "if ( Condition ) { Program } else { Program }")
grammar.add_production("WhileLoop", "while ( Condition ) { Program }")
grammar.add_production("AssignmentFor", "identifier = Expression")   #
grammar.add_production("ForLoop", "for ( AssignmentFor ; Condition ; AssignmentFor ) { Program }")  #
grammar.add_production("Expression", "identifier")
grammar.add_production("Expression", "constant")
grammar.add_production("Expression", "Expression + Expression")
grammar.add_production("Expression", "Expression / Expression")
grammar.add_production("Expression", "Expression * Expression")
grammar.add_production("Expression", "Expression - Expression")
'''
grammar.add_production("Expression", "Term Expression'")
grammar.add_production("Expression'", "+ Term Expression'")
grammar.add_production("Expression'", "- Term Expression'")
grammar.add_production("Expression'", "λ")
grammar.add_production("Term", "Factor Term'")
grammar.add_production("Term'", "* Factor Term'")
grammar.add_production("Term'", "/ Factor Term'")
grammar.add_production("Term'", "λ")
grammar.add_production("Factor", "identifier")
grammar.add_production("Factor", "constant")
grammar.add_production("Factor", "( Expression )")
'''
grammar.add_production("Condition", "Expression == Expression")
grammar.add_production("Condition", "Expression != Expression")
grammar.add_production("Condition", "Expression < Expression")
grammar.add_production("Condition", "Expression > Expression")
grammar.add_production("Condition", "Expression <= Expression")
grammar.add_production("Condition", "Expression >= Expression")

grammar.print_productions()
'''
grammar = GLC("E")
grammar.add_production("E", "T")
grammar.add_production("E", "E + T")
grammar.add_production("T", "n")
grammar.add_production("T", "( E )")
grammar.print_productions()
'''
analisis = CLR(grammar)
analisis.buildTable()
analisis.printTable()
analisis.analyze("if ( identifier == constant ) { constant ; }")
analisis.analyze("if ( identifier == constant ) { identifier = constant ; }")
analisis.analyze("if ( identifier == constant ) { identifier = identifier * constant + constant ; }")
analisis.analyze("while ( identifier > constant ) { identifier = constant / constant - identifier ; identifier = constant ; }")
analisis.analyze("while ( identifier > constant ) { if ( identifier != constant ) { identifier = constant ; } }")
analisis.analyze("for ( identifier = constant ; identifier >= constant ; identifier = identifier + constant ) { if ( identifier != constant ) { identifier = constant ; } }")
