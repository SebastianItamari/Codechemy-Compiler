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
                            self.add_if_not_exist(reachable,symbol)
                            #if symbol not in reachable:
                            #    reachable.append(symbol)
                    else:
                        #if production_key not in keys_to_remove:
                        #    keys_to_remove.append(production_key)
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

grammar = GLC('S')

grammar.add_production('S', "aSb")
grammar.add_production('S', "cSE")
grammar.add_production('S', "ab")
grammar.add_production('B', "dc")
grammar.add_production('E', "FbF")
grammar.add_production('E', "a")
grammar.add_production('F', "abc")
grammar.add_production('F', "λ")

#No es necesario, ya que en mi caso no lo uso
grammar.add_terminal('a')
grammar.add_terminal('b')
grammar.add_terminal('c')
grammar.add_terminal('d')

print("GRAMÁTICA 1")
grammar.print_productions()
print("--------------------------------------")
print("Segunda Fase:")
grammar.second_phase()
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

grammar2.print_productions()
print("PRIMEROS")
print(grammar2.get_first())
print("SEGUNDOS")
print(grammar2.get_following())