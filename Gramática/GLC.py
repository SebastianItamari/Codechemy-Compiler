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
        new_terminals = []
        new_noTerminals = []
        
        for nonterminal in self.productions:
            production_list = self.productions[nonterminal]
            prefix_dict = {}
            
            for production in production_list:
                first_symbol = production[0]
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
                        if len(production) == 1:
                            new_suffixes.append('λ')
                        else:
                            new_suffixes.append(production[1:])
                    
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
                for symbol in production:
                    if symbol not in new_noTerminals and symbol not in new_terminals:
                        new_terminals.append(symbol)
        
        self.productions = self.transform_to_productions(new_productions)
        self.terminals = new_terminals
        self.noTerminals = new_noTerminals

        print(self.terminals)
        print(self.noTerminals)


    def transform_to_productions(self, new_productions):
        productions = {}
        for variable in new_productions:
            rules = []
            for rule in new_productions[variable]:
                if isinstance(rule, list):
                    rules.append(''.join(rule))
                else:
                    rules.append(rule)
            productions[variable] = rules
        return productions



""""
    
    def left_factoring(self):
        new_productions = {}
        for left in self.productions:
            right_list = self.productions[left]
            prefix_dict = {}
            for right in right_list:
                first_symbol = right[0]
                if first_symbol not in prefix_dict:
                    prefix_dict[first_symbol] = [right]
                else:
                    prefix_dict[first_symbol].append(right)
            new_rules = []
            new_nonterminals = {}
            for prefix in prefix_dict:
                rhs_list_with_prefix = prefix_dict[prefix]
                if len(rhs_list_with_prefix) > 1:
                    new_lhs = left + "'"
                    while new_lhs in self.productions or new_lhs in new_nonterminals:
                        new_lhs += "'"
                    new_rules.append([prefix, new_lhs])
                    new_suffixes = []
                    for right in rhs_list_with_prefix:
                        if len(right) == 1:
                            new_suffixes.append('λ')
                        else:
                            new_suffixes.append(right[1:])
                    new_nonterminals[new_lhs] = new_suffixes
                else:
                    new_rules.append(rhs_list_with_prefix[0])
            new_productions[left] = new_rules
            for nonterminal in new_nonterminals:
                new_productions[nonterminal] = new_nonterminals[nonterminal]
        self.productions = self.transform_to_productions(new_productions)

    
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
"""

grammar = GLC('S')

grammar.add_production('S', "aSb")
grammar.add_production('S', "acSE")
grammar.add_production('S', "b")
grammar.add_production('B', "d")
grammar.add_production('B', "Fc")
grammar.add_production('B', "dFa")
grammar.add_production('E', "abF")
grammar.add_production('F', "abc")

#No es necesario, ya que en mi caso no lo uso
grammar.add_terminal('a')
grammar.add_terminal('b')
grammar.add_terminal('c')
grammar.add_terminal('d')


print("GRAMÁTICA 1")
grammar.print_productions()
"""
print("--------------------------------------")
print("Segunda Fase:")
grammar.second_phase()
grammar.print_productions()
"""

grammar.left_factoring()
print("Factorizacion:")
grammar.print_productions()