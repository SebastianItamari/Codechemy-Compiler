class GLC:
    def __init__(self,initial):
        self.initial = initial
        self.terminals = []
        self.nonTerminals = []
        self.productions = {}

        self.firstS = {}
        self.nextS = {}

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
            if c[0].islower() or c == "λ" and not c in self.terminals:
                self.terminals.append(c)
            elif c[0].isupper() and not c in self.nonTerminals:
                self.nonTerminals.append(c)
        
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

    def add_reachable_productions(self, reachable):
        keys_to_remove = []
        for production_key, production_list in self.productions.items():
            for production in production_list:
                for symbol in production.split():
                    if production_key in reachable:
                        if symbol in self.nonTerminals:
                            self.add_if_not_exist(reachable,symbol)
                            #if symbol not in reachable:
                            #    reachable.append(symbol)
                    else:
                        self.add_if_not_exist(keys_to_remove,production_key)
        return keys_to_remove

    def second_phase(self):
        reachable = [self.initial]
        keys_to_remove = self.add_reachable_productions(reachable)

        for key in keys_to_remove:
            del self.productions[key]
            self.nonTerminals.remove(key)

    def print_productions(self):
        for variable in self.productions.keys():
            print(variable + " -> " + " | ".join(self.productions[variable]))

    def add_terminal(self, terminal):
        self.terminals.append(terminal)

    def get_first(self):
        for production_key in self.productions.keys():
            self.firstS[production_key] = set(self.first(production_key))
        return self.firstS

    """
    def first(self, key):
            aux = []
            if not key in self.nonTerminals:
                return [key]
            
            for list in self.productions[key]:
                for character in list.split():
                    if not character in self.nonTerminals:  #si es un terminal
                        self.add_if_not_exist(aux,character)
                    else:
                        while 'λ' in self.first(character):
                            auxList = self.first(character)
                            auxList.remove('λ')
                            aux += auxList

                        aux = aux + self.first(character)
            return aux
    """
    def first(self, key):
        aux = []
        if not key in self.nonTerminals:
            return [key]
        
        for list in self.productions[key]:
            auxList1 =  list.split()
            i = 0
            tam = len(auxList1)

            if not auxList1[i] in self.nonTerminals:  #si es un terminal
                self.add_if_not_exist(aux,auxList1[i])
            else:
                while 'λ' in self.first(auxList1[i]) and i < (tam -1):
                    auxList = self.first(auxList1[i])
                    auxList.remove('λ')
                    aux += auxList
                    i += 1

                aux = aux + self.first(auxList1[i])
        return aux

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
        self.noTerminals = new_noTerminals

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

grammar = GLC('S')

grammar.add_production('S', "B\' A")
grammar.add_production('S', "a b A")
grammar.add_production('S', "B\' a S")
grammar.add_production('A', "z A")
grammar.add_production('B\'', "a b")
grammar.add_production('B\'', "f")
grammar.add_production('C\'', "a e")

print("GRAMÁTICA 1")
grammar.print_productions()
print("--------------------------------------")

""""
print("GRAMÁTICA 1 after phase 1")
grammar.firstPhase()
grammar.print_productions()
print("--------------------------------------")
print("GRAMÁTICA 1 after phase 2")
print(grammar.second_phase())
grammar.print_productions()
print("--------------------------------------\n\n\n")
"""

grammar.left_factoring()
grammar.print_productions()


""""
grammar2 = GLC('S')

grammar2.add_production('S', "a Z")
grammar2.add_production('S', "S Y")
grammar2.add_production('S', "X A")
grammar2.add_production('X', "b S Z a")
grammar2.add_production('Y', "a S Y")
grammar2.add_production('Y', "b Y Z")
grammar2.add_production('Z', "a Y Z")
grammar2.add_production('Z', "a d")
grammar2.add_production('A', "a b")
grammar2.add_production('A', "a A")


print("GRAMÁTICA 2")
grammar2.print_productions()
print("--------------------------------------")
print("GRAMÁTICA 2 after phase 1")
grammar2.firstPhase()
grammar2.print_productions()

print("--------------------------------------")
print("GRAMÁTICA 2 after phase 2")
grammar2.second_phase()
grammar2.print_productions()
print("--------------------------------------")


print("GRAMÁTICA 3")
grammar3 = GLC('S')

grammar3.add_production('S', "D B c")  #Reemplazar producción por DB si se quiere probar que si añade 'λ' a los primeros de S
grammar3.add_production('S', "d")
grammar3.add_production('B', "e S")
grammar3.add_production('B', "λ")
grammar3.add_production('D', "a")
grammar3.add_production('D', "b D")
grammar3.add_production('D', "λ")
grammar3.add_production('D', "d B a")
grammar3.print_productions()
print("PRIMEROS")
print(grammar3.get_first())
"""

grammar4 = GLC('M')
grammar4.add_production('M', "N")
grammar4.add_production('M', "N M")
grammar4.left_factoring()
grammar4.print_productions() 

grammar5 = GLC('V')
grammar5.add_production('V', "Y")
grammar5.add_production('V', "Y n V")
grammar5.add_production('V', "a n")
grammar5.left_factoring()
grammar5.print_productions() 

grammar6 = GLC('C\'')
grammar6.add_production('C\'', "C\' 🜁 D'")
grammar6.add_production('C\'', "C\' 🜃 D'")
grammar6.add_production('C\'', "D\'")
grammar6.add_production('C\'\'', "D\'")
grammar6.left_factoring()
grammar6.print_productions() 

grammar7 = GLC('I\'')
grammar7.add_production('I\'', "F")
grammar7.add_production('I\'', "F c I\'")
grammar7.add_production('I\'', "λ")
grammar7.left_factoring()
grammar7.print_productions() 
