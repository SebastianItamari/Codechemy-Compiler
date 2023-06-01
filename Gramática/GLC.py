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
        print("NO TERMINALES")
        print(self.noTerminals)
        print("TERMINALS")
        print(self.terminals)

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
            self.noTerminals.remove(key)
            
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
                self.del_productions(variable)  # Eliminar producciones de la variable con recursión
                self.noTerminals.append(new_variable)

                for production in new_productions:
                    self.add_production(variable, production + new_variable)

                for production in recursive_productions:
                    self.add_production(new_variable, production[1:] + new_variable)

                self.add_production(new_variable, 'ε')


    def add_terminal(self, terminal):
        self.terminals.append(terminal)
    
    def del_productions(self, variable):
        if variable in self.productions:
            del self.productions[variable]
            if variable in self.noTerminals:
                self.noTerminals.remove(variable)



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



    def left_factoring(self):
        new_productions = {}
        for variable in self.noTerminals:
            productions = self.productions[variable]
            common_prefix = self.get_common_prefix(productions)
            print("COMMON", common_prefix)
            if common_prefix:
                new_variable = variable + "'"
                new_productions[variable] = [common_prefix + new_variable]
                new_productions[new_variable] = [production[len(common_prefix):] for production in productions]
            else:
                new_productions[variable] = productions
        self.productions = new_productions

    def get_common_prefix(self, productions):
        if len(productions) < 2:
            return ""
        common_prefix = ""
        min_length = min(len(production) for production in productions)
        for i in range(min_length):
            symbols = set(production[i] for production in productions if i < len(production))
            if len(symbols) == 1:
                common_prefix += productions[0][i]
            else:
                break
        return common_prefix

grammar = GLC('S')

'''
#Prueba 1
grammar.add_production('S', "AB")
grammar.add_production('A', "BS")
grammar.add_production('A', "b")
grammar.add_production('B', "SS")
grammar.add_production('B', "a")
grammar.add_production('C', "dc")


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
grammar.add_production('S', "aSb")
grammar.add_production('S', "acSE")
grammar.add_production('S', "ab")
grammar.add_production('B', "dEacSF")
grammar.add_production('B', "dEaFca")
grammar.add_production('B', "dEaF")
grammar.add_production('B', "dEa")
grammar.add_production('E', "abF")
grammar.add_production('F', "abc")
'''

#Prueba 4
grammar.add_production('S', "Sa")
grammar.add_production('S', "Sb")
grammar.add_production('S', "c")
grammar.add_production('S', "d")
grammar.add_production('A', "BS")
grammar.add_production('A', "b")
grammar.add_production('B', "SS")
grammar.add_production('B', "a")
grammar.add_production('C', "dc")

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


""""
print("GRAMÁTICA 1")
grammar.print_productions()
print("--------------------------------------")
print("Segunda Fase:")
grammar.second_phase()
grammar.print_productions()

print("--------------------------------------")
print("Eliminación de Recursión a la Izquierda:")
grammar.eliminate_left_recursion()
grammar.print_productions()

print("--------------------------------------")
print("Eliminación de Recursión Indirecta a la Izquierda:")
grammar.eliminate_indirect_left_recursion()
grammar.print_productions()
"""

grammar.left_factoring()
print("Factorizacion:")
grammar.print_productions()
