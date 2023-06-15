#standard library imports
from copy import *

#local application imports
from .GrammarCLR import *
from Gramática.GLC import * 

class ItemCLR:
    def __init__(self, name, originalGrammar, firstSOG, grammar):
        self.name = name
        self.originalGrammar = originalGrammar #GLC
        self.firstSOG = firstSOG
        self.nonClosingGrammar = deepcopy(grammar) #GrammarCLR
        self.grammar = deepcopy(grammar) #GrammarCLR

    def closing(self,added):
        aux = self.partial_Closing(added)
        if(len(aux) > 0):
            for value in aux:
                self.add_Productions(value)
            self.closing(added)

    def partial_Closing(self, added):
        toAdd = []
        for nonTerminal in self.grammar.productions:
            list = self.grammar.productions[nonTerminal]
            for prod in list:
                elementList = prod[0].split()
                tam = len(elementList)
                for index, letter in enumerate(elementList):
                    if letter == ".":
                        if index != tam - 1:   #Si el punto no está al final
                            aux = []
                            if index == tam - 2:  #Si despues del punto solo hay un elemento
                                aux = copy(prod[1])  #Si no copias hay error
                            elif index < tam -2:
                                aux = self.get_First(elementList[index + 2])

                            if (elementList[index + 1] in self.originalGrammar.productions) and (not (elementList[index + 1],aux) in added):
                                toAdd.append((elementList[index + 1],aux))
                                added.append((elementList[index + 1],aux))
        return toAdd

    def add_Productions(self,value):
        for prod in self.originalGrammar.productions[value[0]]:
            self.grammar.add_production(value[0], (". " + prod, value[1]))

    def remove_Duplicates(self, lst):
        unique_list = []
        for item in lst:
            if item not in unique_list:
                unique_list.append(item)
        return unique_list
    
    def get_First(self,value):
        if value in self.originalGrammar.nonTerminals:
            return self.firstSOG[value]
        else:
            return [value]
    
    def elements(self):
        elements = []
        for nonTerminal in self.grammar.productions:
            list = self.grammar.productions[nonTerminal]
            for prod in list:
                elementList = prod[0].split()
                tam = len(elementList)
                for index, letter in enumerate(elementList):
                    if letter == ".":
                        if index != tam - 1:   #Si el punto no está al final
                            elements.append(elementList[index + 1])
        return self.remove_Duplicates_List(elements)
    
    def remove_Duplicates_List(self, lst):
        return list(OrderedDict.fromkeys(lst))

