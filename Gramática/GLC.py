class GLC:
    def __init__(self,initial):
        self.initial = initial
        self.terminals = []
        self.noTerminals = []
        self.productions = {} #diccionario

    def add_production(self, variable, production):
        if variable in self.productions:
            self.productions[variable].append(production)
        else:
            self.productions[variable] = [production] #nueva clave
            self.noTerminals.append(variable) 

    def print_productions(self):
        for variable in self.productions.keys():
            print(variable + " -> " + " | ".join(self.productions[variable]))

    def add_terminal(self, terminal):
        self.terminals.append(terminal)

    def add_reachable_productions(self, reachable):
        keys_to_remove = []
        for production_key, production_list in self.productions.items():
            for production in production_list:
                for symbol in production:
                    if production_key in reachable:
                        if symbol in self.noTerminals:
                            if symbol not in reachable:
                                reachable.add(symbol)
                    else:
                        if production_key not in keys_to_remove:
                            keys_to_remove.append(production_key)

        return keys_to_remove

    def second_phase(self):
        reachable = {self.initial}
        keys_to_remove = self.add_reachable_productions(reachable)

        for key in keys_to_remove:
            del self.productions[key]

    def eliminate_indirect_left_recursion(self):
        variables = self.noTerminals.copy()

        for i in range(len(variables)):
            variable_i = variables[i]
            for j in range(i):
                variable_j = variables[j]
                if variable_i in self.productions and variable_j in self.productions:
                    productions_i = self.productions[variable_i]
                    productions_j = self.productions[variable_j]
                    new_productions = []
                    for production_i in productions_i:
                        if production_i.startswith(variable_j):
                            for production_j in productions_j:
                                new_production = production_j + production_i[1:]
                                new_productions.append(new_production)
                        else:
                            new_productions.append(production_i)
                    self.productions[variable_i] = new_productions


grammar = GLC('S')

#Prueba 1
grammar.add_production('S', "AB")
grammar.add_production('A', "BS")
grammar.add_production('A', "b")
grammar.add_production('B', "SS")
grammar.add_production('B', "a")
grammar.add_production('C', "dc")

'''
#Prueba 2
grammar.add_production('P', "Qr")
grammar.add_production('P', "S")
grammar.add_production('Q', "Pt")
grammar.add_production('Q', "U")

#Prueba 3
grammar.add_production('A', "Br")
grammar.add_production('B', "Cd")
grammar.add_production('C', "At")

grammar.add_production('S', "aSbB")
grammar.add_production('S', "cSE")
grammar.add_production('S', "ab")
grammar.add_production('B', "dEacSF")
grammar.add_production('B', "dEaFca")
grammar.add_production('B', "dEaF")
grammar.add_production('B', "dEa")
grammar.add_production('E', "abF")
grammar.add_production('F', "abc")
'''
# No es necesario, ya que en mi caso no lo uso
grammar.add_terminal('a')
grammar.add_terminal('b')
grammar.add_terminal('c')
grammar.add_terminal('d')

'''
#No es necesario, ya que en mi caso no lo uso
grammar.add_terminal('a')
grammar.add_terminal('b')
grammar.add_terminal('c')
'''
#grammar.add_terminal('d')

print("GRAMÁTICA 1")
grammar.print_productions()
print("--------------------------------------")
print("Segunda Fase:")
grammar.second_phase()
grammar.print_productions()
print("--------------------------------------")
print("Eliminación de Recursión Indirecta a la Izquierda:")
grammar.eliminate_indirect_left_recursion()
grammar.print_productions()
