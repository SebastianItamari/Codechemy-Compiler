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
                while 'λ' in self.first(auxList1[i]) and i < (tam -1):
                    auxList = self.first(auxList1[i])
                    auxList.remove('λ')
                    aux += auxList
                    i += 1

                aux = aux + self.first(auxList1[i])
        return aux
    
    def add_if_not_exist(self, list, element):
        if element not in list:
            list.append(element)

    def get_following(self):
        for production_key in self.productions.keys():
            self.followingS[production_key] = set(self.following(production_key))
        return self.followingS
        
    
    def following(self, key):
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
                            if(key != noTerminal):
                                if noTerminal in self.followingS:
                                    aux += self.followingS[noTerminal]
                                else:
                                    aux += self.following(noTerminal)
                        else:
                            if elementList[index + 1] in self.nonTerminals:
                                first = self.firstS[elementList[index + 1]]
                                if 'λ' in first:
                                    first.remove('λ')
                                    aux += first
                                    if(key != noTerminal):
                                        if noTerminal in self.followingS:
                                            aux += self.followingS[noTerminal]
                                        else:
                                            aux += self.following(noTerminal)
                                else: 
                                    aux += first
                            else:
                                aux.append(elementList[index + 1])
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
                self.nonTerminals.append(new_variable)

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
            if variable in self.nonTerminals:
                self.nonTerminals.remove(variable)



    def eliminate_indirect_left_recursion(self):
        variables = self.nonTerminals.copy()

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
        for variable in self.nonTerminals:
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

print("--------------------------------------")
print("GRAMÁTICA 2")
grammar2 = GLC("S")

grammar2.add_production("S", "D' B'' coca")  #Reemplazar producción por DB si se quiere probar que si añade 'λ' a los primeros de S
grammar2.add_production("S", "dedo")
grammar2.add_production("B''", "exp S")
grammar2.add_production("B''", "λ")
grammar2.add_production("D'", "aux")
grammar2.add_production("D'", "beso D'")
grammar2.add_production("D'", "λ")
grammar2.add_production("D'", "dedo B'' aux")
grammar2.print_productions()
print("PRIMEROS")
print(grammar2.get_first())
print("SIGUIENTES")
print(grammar2.get_following())

print("--------------------------------------")
print("GRAMÁTICA 3")
grammar3 = GLC("E")

grammar3.add_production("E", "T E'")  #Reemplazar producción por DB si se quiere probar que si añade 'λ' a los primeros de S
grammar3.add_production("E'", "+ T E'")
grammar3.add_production("E'", "- T E'")
grammar3.add_production("E'", "λ")
grammar3.add_production("T", "F T'")
grammar3.add_production("T'", "* F T'")
grammar3.add_production("T'", "/ F T'")
grammar3.add_production("T'", "λ")
grammar3.add_production("F", "( E )")
grammar3.add_production("F", "num")
grammar3.add_production("F", "id")

grammar3.print_productions()
print("PRIMEROS")
print(grammar3.get_first())
print("SIGUIENTES")
print(grammar3.get_following())


print("--------------------------------------")
print("NUESTRA GRAMÁTICA")
grammar4 = GLC("A")

grammar4.add_production("A", "🜉 Y 🝓")  #Reemplazar producción por DB si se quiere probar que si añade 'λ' a los primeros de S
grammar4.add_production("B", "🝰")
grammar4.add_production("B", "🝯")
grammar4.add_production("B", "🝮")
grammar4.add_production("C", "B")
grammar4.add_production("C", "🜸")
grammar4.add_production("D", "🝳 K 🝳")
grammar4.add_production("E", "🜛 K ☾ I' ☽ 🜛")
grammar4.add_production("F", "B e D")
grammar4.add_production("G", "D e 🝑 e H")
grammar4.add_production("H", "B'")
grammar4.add_production("H", "E'")
grammar4.add_production("I", "D")
grammar4.add_production("I", "M")
grammar4.add_production("J", "🜂")    
grammar4.add_production("J", "🜄")
grammar4.add_production("J", "🜁")
grammar4.add_production("J", "🜃")
grammar4.add_production("K", "L K")  
grammar4.add_production("K", "M K")
grammar4.add_production("K", "λ")
grammar4.add_production("L", "a")   #PENDIENTE, FALTAN MÁS LETRAS
grammar4.add_production("L", "b")
grammar4.add_production("L", "c")
grammar4.add_production("L", "A")
grammar4.add_production("L", "B")
grammar4.add_production("L", "C")
grammar4.add_production("M", "NO'")
grammar4.add_production("O'", "M")
grammar4.add_production("O'", "λ")
grammar4.add_production("N", "0")  
grammar4.add_production("N", "1")  
grammar4.add_production("N", "2")  
grammar4.add_production("N", "3")  
grammar4.add_production("N", "4")  
grammar4.add_production("N", "5")  
grammar4.add_production("N", "6")  
grammar4.add_production("N", "7")  
grammar4.add_production("N", "8")
grammar4.add_production("N", "9")    
grammar4.add_production("O", "🝱")
grammar4.add_production("P", "🜓")
grammar4.add_production("P", "🝘")
grammar4.add_production("Q", "🜔")
grammar4.add_production("Q", "🜕")
grammar4.add_production("Q", "🜖")
grammar4.add_production("Q", "🜗")
grammar4.add_production("Q", "🜎")
grammar4.add_production("Q", "🜍")
grammar4.add_production("R", "v")
grammar4.add_production("R", "m")
grammar4.add_production("R", "D")
grammar4.add_production("S", "s e ☾ E' ☽ n 🜚 n Y 🜚 n T")
grammar4.add_production("T", "i n 🜚 n Y n 🜚")  
grammar4.add_production("T", "λ")
grammar4.add_production("U", "d e ☾ E' ☽ n 🜚 n V n 🜚")
grammar4.add_production("V", "Y V'") 
grammar4.add_production("V", "a n")
grammar4.add_production("V'", "n V")
grammar4.add_production("V'", "λ")
grammar4.add_production("W", "Y W'")
grammar4.add_production("W", "r e D n")
grammar4.add_production("W'", "n W")
grammar4.add_production("W'", "λ")
grammar4.add_production("X", "I Q I")
grammar4.add_production("Y", "Z Y'")
grammar4.add_production("Y'", "n Y")
grammar4.add_production("Y'", "λ")
grammar4.add_production("Z", "")
grammar4.add_production("Z", "F") 
grammar4.add_production("Z", "A'")
grammar4.add_production("Z", "U")
grammar4.add_production("Z", "S")
grammar4.add_production("Z", "n")
grammar4.add_production("Z", "J'")
grammar4.add_production("A'", "B'")
grammar4.add_production("A'", "E'")

grammar4.print_productions()



