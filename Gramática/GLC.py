class GLC:
    def __init__(self,initial):
        self.initial = initial
        self.terminals = []
        self.noTerminals = []

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
        if not variable in self.noTerminals:
            self.noTerminals.append(variable)

        for c in production.split():
            if c[0].islower() or c == "λ" and not c in self.terminals:
                self.terminals.append(c)
            elif c[0].isupper() and not c in self.noTerminals:
                self.noTerminals.append(c)

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
            self.noTerminals.remove(p)

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
                        if symbol in self.noTerminals:
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
            self.noTerminals.remove(key)

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
            self.noTerminals.remove(key)
    def get_first(self):
        for production_key in self.productions.keys():
            self.firstS[production_key] = set(self.first(production_key))
        return self.firstS

    def first(self, key):
        aux = []
        if not key in self.noTerminals:
            return [key]
        for list in self.productions[key]:
            i = 0
            tam = len(list)
            if not list[i] in self.noTerminals:  #si es un terminal
                self.add_if_not_exist(aux,list[i])
            else:
                while 'λ' in self.first(list[i]) and i < (tam - 1):
                    auxList = self.first(list[i])
                    auxList.remove('λ')
                    aux += auxList
                    i += 1
                
                aux = aux + self.first(list[i])
        return aux
    
    def add_if_not_exist(self, list, element):
        if element not in list:
            list.append(element)

    def get_following(self):
        for production_key in self.productions.keys():
            self.nextS[production_key] = set(self.following(production_key))
        return self.nextS
        
    
    def following(self, key):
        aux = []
        if key == self.initial:
            aux = ['$']

        for noTerminal in self.productions:
            list = self.productions[noTerminal]
            for element in list:
                tam = len(element)
                for index, letter in enumerate(element):
                    if key == letter:
                        #print(key,noTerminal,element,index)  #key es la llave (no terminal del que se quiere sacar siguientes), 
                                                             #no Terminal es en el noTerminal que se encuenta key en el conjunto de producciones,
                                                             #element es la producción en la cual se encuentra key y index es el índice en la producción
                                                             #en donde se encuentra key. Se hace el ciclo para el caso donde aparezca la misma letra varias veces
                                                             #en la misma producción
                        if index == tam - 1:
                            if(key != noTerminal):
                                aux += self.following(noTerminal)
                        else:
                            if element[index + 1] in self.noTerminals:
                                first = self.firstS[element[index + 1]]
                                if 'λ' in first:
                                    first.remove('λ')
                                    aux += first
                                    if(key != noTerminal):
                                        aux += self.following(noTerminal)
                                else: 
                                    aux += first
                                aux += self.firstS[element[index + 1]]
                            else:
                                aux += element[index + 1]
        return aux
            
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
grammar.add_production('S', "ab")

grammar.add_production('B', "dc")
grammar.add_production('E', "FbF")
grammar.add_production('E', "a")
grammar.add_production('F', "abc")
grammar.add_production('F', "λ")
=======
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


print("GRAMÁTICA 1")
grammar.print_productions()
print("--------------------------------------")
print("Primera Fase:")
grammar.firstPhase()
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
print("--------------------------------------")
print("GRAMÁTICA 2")
grammar2 = GLC('S')

grammar2.add_production('S', "DBc")  #Reemplazar producción por DB si se quiere probar que si añade 'λ' a los primeros de S
grammar2.add_production('S', "d")
grammar2.add_production('B', "eS")
grammar2.add_production('B', "λ")
grammar2.add_production('D', "a")
grammar2.add_production('D', "bD")
grammar2.add_production('D', "λ")
grammar2.add_production('D', "dBa")
print("PRIMEROS")
print(grammar2.get_first())
print("SEGUNDOS")
print(grammar2.get_following())





