from collections import OrderedDict
from copy import *

class GLC:
    def __init__(self,initial):
        self.initial = initial
        self.terminals = []
        self.nonTerminals = []
        self.productions = {}
        self.firstS = {}
        self.followingS = {}

    def add_production(self, variable, production):
        if variable in self.productions:
            self.productions[variable].append(production)
        else:
            self.productions[variable] = [production]
        
        self.addTerminalsAndNonTerminals(variable, production)

    def addTerminalsAndNonTerminals(self, variable, production):
        if not variable in self.nonTerminals:
            self.nonTerminals.append(variable)

        for c in production.split():
            if c[0].isupper() and c not in self.nonTerminals:
                self.nonTerminals.append(c)
            elif (not c[0].isupper() or c ==  "λ") and not c in self.terminals:
                self.terminals.append(c)

    def print_productions(self):
        for variable in self.productions.keys():
            print(variable + " -> " + " | ".join(self.productions[variable]))

    def get_first(self):
        for production_key in self.productions.keys():
            self.firstS[production_key] = self.remove_duplicates(self.first(production_key))
        return self.firstS

    def first(self, key):
        aux = []
        if not key in self.nonTerminals:
            return [key]
        for list in self.productions[key]:
            auxList1 =  list.split()
            i = 0
            tam = len(auxList1)

            if not auxList1[i] in self.nonTerminals:  #si es un terminal
                aux.append(auxList1[i])
            else:
                if auxList1[i] != key:   #Se aumento esto para el caso de posible recursividad, aunque no debiera ocurrir
                    while "λ" in self.first(auxList1[i]) and i < (tam -1):
                        auxList = self.first(auxList1[i])
                        auxList.remove("λ")
                        aux += auxList
                        i += 1

                    aux = aux + self.first(auxList1[i])
        return aux

    def get_following(self):
        for production_key in self.productions.keys():
            #print("KEY: " + production_key)
            self.followingS[production_key] = self.remove_duplicates(self.following(production_key,[production_key]))
        return self.followingS
        
    
    def following(self, key, keysAnalized):
        #print(key)
        aux = []
        if key == self.initial:
            aux = ["$"]

        for noTerminal in self.productions:
            list = self.productions[noTerminal]
            for element in list:
                elementList = element.split()
                tam = len(elementList)
                for index, letter in enumerate(elementList):
                    if key == letter:
                        #print(key,noTerminal,elementList,index)  #key es la llave (no terminal del que se quiere sacar siguientes), 
                                                             #no Terminal es en el noTerminal que se encuenta key en el conjunto de producciones,
                                                             #element es la producción en la cual se encuentra key y index es el índice en la producción
                                                             #en donde se encuentra key. Se hace el ciclo para el caso donde aparezca la misma letra varias veces
                                                             #en la misma producción
                        if index == tam - 1:
                            if key != noTerminal and not noTerminal in keysAnalized:   #
                                if noTerminal in self.followingS:
                                    aux += self.followingS[noTerminal]
                                else:
                                    keysAnalized.append(noTerminal)
                                    aux += self.following(noTerminal,keysAnalized)
                        else:
                            if elementList[index + 1] in self.nonTerminals:
                                first = copy(self.firstS[elementList[index + 1]])
                                if 'λ' in first:
                                    first.remove('λ')
                                    aux += first
                                    if key != noTerminal and not noTerminal in keysAnalized:  #
                                        if noTerminal in self.followingS:
                                            aux += self.followingS[noTerminal]
                                        else:
                                            keysAnalized.append(noTerminal)
                                            aux += self.following(noTerminal,keysAnalized)
                                else: 
                                    aux += first
                            else:
                                aux.append(elementList[index + 1])
        return aux
    
    def remove_duplicates(self, lst):
        return list(OrderedDict.fromkeys(lst))
    
    def addOnlyTerminalsProductions(self):
        generativeProductions = {}
        for nt, derivations in self.productions.items():
            for derivation in derivations:
                terminals = list(filter(lambda x: x in self.terminals, derivation.split()))
                if len(terminals) == len(derivation.split()):
                    if nt in generativeProductions:
                        generativeProductions[nt].append(derivation)
                    else:
                        generativeProductions[nt] = [derivation]
        return generativeProductions

    def addUsefulProductions(self):
        newProductions = self.addOnlyTerminalsProductions()
        changed = 1

        while (changed):
            changed = 0
            for nt, derivations in self.productions.items():
                for derivation in derivations:
                    variables = list(filter(lambda x: not x in self.terminals, derivation.split()))
                    if nt in newProductions and derivation in newProductions[nt]:
                        pass 
                    elif all(c in newProductions.keys() for c in variables):
                        if nt in newProductions:
                            newProductions[nt].append(derivation)
                        else:
                            newProductions[nt] = [derivation]
                        changed = 1
        return newProductions
    
    def firstPhase(self):
        usefulProductions = self.addUsefulProductions()
        productions2Delete = []
        for nt in self.productions.keys():
                if nt in usefulProductions:
                    self.productions[nt] = usefulProductions[nt]
                else:
                    productions2Delete.append(nt)
                    
        
        for p in productions2Delete:
            del self.productions[p]
            self.nonTerminals.remove(p)

        characters = ""
        for value in self.productions.values():
            characters += " ".join(value)
        
        for t in self.terminals:
            if not t in characters:
                self.terminals.remove(t)

    def add_if_not_exist(self, list, element):
        if element not in list:
            list.append(element)

    def add_reachable_productions(self, reachable, key):
            for production in self.productions[key]:
                for symbol in production.split():
                    if symbol in self.nonTerminals:
                        if not symbol in reachable:
                            reachable.append(symbol)
                            self.add_reachable_productions(reachable, symbol)
        
    def second_phase(self):
        reachable = [self.initial]
        self.add_reachable_productions(reachable, self.initial)

        keys_to_remove = []
        for key in self.productions:
            if not key in reachable:
                keys_to_remove.append(key)

        for key in keys_to_remove:
            del self.productions[key]
            self.nonTerminals.remove(key)

    def del_productions(self, variable):
        if variable in self.productions:
            del self.productions[variable]
            if variable in self.nonTerminals:
                self.nonTerminals.remove(variable)

    def eliminate_left_recursion(self):
        variables = list(self.productions.keys())
        for variable in variables:
            productions = self.productions[variable]
            new_productions = []
            recursive_productions = []

            for production in productions:
                if production.startswith(variable):
                    recursive_productions.append(production)
                else:
                    new_productions.append(production)

            if len(recursive_productions) > 0:
                new_variable = variable + "'"
                while new_variable in self.productions or new_variable in self.nonTerminals:
                        new_variable += "'"

                self.del_productions(variable)  # Eliminar producciones de la variable con recursión
                self.nonTerminals.append(new_variable)

                for production in new_productions:
                    self.add_production(variable, production + ' ' + new_variable)

                for production in recursive_productions:
                    self.add_production(new_variable, production.split()[0] + ' ' + new_variable)

                self.add_production(new_variable, 'λ')

    def left_factoring(self):
        new_productions = {}
        new_terminals = []
        new_noTerminals = []

        for nonterminal in self.productions:
            production_list = self.productions[nonterminal]
            prefix_dict = {}

            for production in production_list:
                if isinstance(production, str):
                    symbols = production.split()
                else:
                    symbols = production

                if symbols and len(symbols) > 0:
                    first_symbol = symbols[0]

                if first_symbol not in prefix_dict:
                    prefix_dict[first_symbol] = [production]
                else:
                    prefix_dict[first_symbol].append(production)

            new_rules = []
            new_nonterminals = {}

            for prefix in prefix_dict:
                productions_with_prefix = prefix_dict[prefix]

                if len(productions_with_prefix) > 1:
                    new_lhs = nonterminal + "'"
                    while new_lhs in self.productions or new_lhs in new_nonterminals:
                        new_lhs += "'"
                    new_rules.append([prefix, new_lhs])
                    new_suffixes = []

                    for production in productions_with_prefix:
                        if isinstance(production, str):
                            suffix = ' '.join(production.split()[1:])
                        else:
                            suffix = ' '.join(production[1:])
                        if len(suffix) == 0:
                            new_suffixes.append('λ')
                        else:
                            new_suffixes.append(suffix)

                    new_nonterminals[new_lhs] = new_suffixes
                else:
                    new_rules.append(productions_with_prefix[0])

            new_productions[nonterminal] = new_rules
            new_noTerminals.append(nonterminal)

            for new_nonterminal in new_nonterminals:
                new_productions[new_nonterminal] = new_nonterminals[new_nonterminal]
                new_noTerminals.append(new_nonterminal)

        for production_list in new_productions.values():
            for production in production_list:
                if isinstance(production, str):
                    symbols = production.split()
                else:
                    symbols = production

                for symbol in symbols:
                    if symbol not in new_noTerminals and symbol not in new_terminals:
                        new_terminals.append(symbol)

        self.productions = self.transform_to_productions(new_productions)
        self.terminals = new_terminals
        self.nonTerminals = new_noTerminals

    def transform_to_productions(self, new_productions):
        productions = {}
        for variable in new_productions:
            rules = []
            for rule in new_productions[variable]:
                if isinstance(rule, list):
                    rules.append(' '.join(rule))
                else:
                    rules.append(rule)
            productions[variable] = rules
        return productions