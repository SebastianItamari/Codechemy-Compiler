from GLC import *
from collections import OrderedDict
from copy import *

class Item:
    def __init__(self,name,originalGrammar,grammar):
        self.name = name
        self.originalGrammar = originalGrammar
        self.nonClosingGrammar = grammar
        self.grammar = deepcopy(grammar)

    def closing(self,added):
        aux = self.partial_Closing(added)
        if(len(aux) > 0):
            for key in aux:
                self.addProductions(key)
            self.closing(added)

    def partial_Closing(self, added):
        toAdd = []
        for nonTerminal in self.grammar.productions:
            list = self.grammar.productions[nonTerminal]
            for prod in list:
                elementList = prod.split()
                tam = len(elementList)
                for index, letter in enumerate(elementList):
                    if letter == ".":
                        if index != tam - 1:   #Si el punto no está al final
                            if (elementList[index + 1] in self.originalGrammar.productions) and (not elementList[index + 1] in added):
                                toAdd.append(elementList[index + 1])
                                added.append(elementList[index + 1])
        return self.remove_duplicates(toAdd)

    def addProductions(self,key):
        for prod in self.originalGrammar.productions[key]:
            self.grammar.add_production(key, ". " + prod)
         
    def elements(self):
        elements = []
        for nonTerminal in self.grammar.productions:
            list = self.grammar.productions[nonTerminal]
            for prod in list:
                elementList = prod.split()
                tam = len(elementList)
                for index, letter in enumerate(elementList):
                    if letter == ".":
                        if index != tam - 1:   #Si el punto no está al final
                            elements.append(elementList[index + 1])
        return self.remove_duplicates(elements)

    def remove_duplicates(self, lst):
        return list(OrderedDict.fromkeys(lst))

'''
grammar = GLC("E")
grammar.add_production("E","E + T")
grammar.add_production("E","T")
grammar.add_production("T","T * F")
grammar.add_production("T","F")
grammar.add_production("F","( E )")
grammar.add_production("F","id")

grammar1 = GLC("E'")
grammar1.add_production("F","( . E )")

item = Item("I1",grammar,grammar1)
item.closing([])
print("GRAMMATICA ORIGINAL")
item.originalGrammar.print_productions()
print("GRAMMATICA DEL ITEM")
item.grammar.print_productions()
print("ELEMENTOS DEL GOTO")
for item in item.elements():
    print(item)
'''