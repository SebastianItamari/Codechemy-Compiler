class GrammarCRL:
    def __init__(self,initial):
        self.initial = initial
        self.productions = {}

    def add_production(self, variable, tuple):
        if variable in self.productions:
            for element in self.productions[variable]:
                if tuple[0] == element[0]:
                    for i in tuple[1]:
                        if i not in element[1]:
                            element[1].append(i)
                    return
            self.productions[variable].append((tuple[0],tuple[1]))
        else:
            self.productions[variable] = [(tuple[0],tuple[1])]

    def print_productions(self):
        for key, value in self.productions.items():
            production_str = key + " -> "
            production_str += " | ".join([prod[0] + " " +str(prod[1]) for prod in value])
            print(production_str)

'''
prueba = GrammarCRL()
prueba.add_production("L",("o R s",["$"]))
prueba.add_production("L",("a B",["$"]))
prueba.add_production("L",("a B", ["a","b","d","$"]))
prueba.add_production("S",("o R s",["$"]))
prueba.print_productions()
'''
'''
prueba1 = GrammarCRL()
prueba1.add_production("L'",(". L",["$"]))
prueba1.add_production("L",(". L , I",["$"]))
prueba1.add_production("L",(". inicio I",["$"]))
prueba1.add_production("L",(". L , I",[","]))
prueba1.add_production("L",(". inicio I",[","]))
prueba1.print_productions()
print(prueba1.productions)
'''