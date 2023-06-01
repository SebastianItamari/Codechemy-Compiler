class GLC:
    def __init__(self,initial):
        self.initial = initial
        self.terminals = []
        self.nonTerminals = []
        self.productions = {}

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
            if c[0].islower() and not c in self.terminals:
                self.terminals.append(c)
            elif c[0].isupper() and not c in self.nonTerminals:
                self.nonTerminals.append(c)
        
    def addOnlyTerminalsProductions(self):
        generativeProductions = {}
        for nt, derivations in self.productions.items():
            for derivation in derivations:
                terminals = list(filter(lambda x: x.islower(), derivation.split()))
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
                    variables = list(filter(lambda x: not x.islower(), derivation.split()))
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

    def print_productions(self):
        for variable in self.productions.keys():
            print(variable + " -> " + " | ".join(self.productions[variable]))

    def add_terminal(self, terminal):
        self.terminals.append(terminal)

grammar = GLC('S')

grammar.add_production('S', "a a B")
grammar.add_production('S', "a b A")
grammar.add_production('S', "a a S")
grammar.add_production('A', "z A")
grammar.add_production('B', "a b")
grammar.add_production('B', "f")
grammar.add_production('C', "a e")


print("GRAMÁTICA 1")
grammar.print_productions()
print("--------------------------------------")

print("GRAMÁTICA 1 after phase 1")
grammar.firstPhase()
grammar.print_productions()
print("--------------------------------------")
print("Terminals 1 ")
print(grammar.terminals)
print("--------------------------------------")
print("NonTerminals 1")
print(grammar.nonTerminals)

print("--------------------------------------\n")
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
