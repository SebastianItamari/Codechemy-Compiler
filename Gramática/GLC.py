class GLC:
    def __init__(self,initial):
        self.initial = initial
        self.terminals = []
        self.noTerminals = []
        self.productions = {}

    def add_production(self, variable, production):
        if variable in self.productions:
            self.productions[variable].append(production)
        else:
            self.productions[variable] = [production]
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

grammar.add_production('S', "aSb")
grammar.add_production('S', "acSE")
grammar.add_production('S', "ab")
grammar.add_production('B', "dc")
grammar.add_production('E', "abF")
grammar.add_production('F', "abc")

#No es necesario, ya que en mi caso no lo uso
grammar.add_terminal('a')
grammar.add_terminal('b')
grammar.add_terminal('c')
grammar.add_terminal('d')

""""
print("GRAMÁTICA 1")
grammar.print_productions()
print("--------------------------------------")
print("Segunda Fase:")
grammar.second_phase()
grammar.print_productions()
"""

grammar.left_factoring()
print("Factorizacion:")
grammar.print_productions()