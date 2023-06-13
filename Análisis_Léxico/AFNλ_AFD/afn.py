#se asume que la posicion 0 es el inicio

class AFN:
    def __init__(self, numeronodos, alfabeto, estadosfinales):
        self.alfabeto = alfabeto
        self.tabla = []
        self.EstadoFinal = []

        for i in range(0, numeronodos):
            self.EstadoFinal.append(False)
            self.tabla.append([])
            for j in range(0, len(alfabeto)):
                self.tabla[i].append([])
        for i in range(0, len(estadosfinales)):
            self.EstadoFinal[estadosfinales[i]] = True    

    def alfabetoindex(self, simbolo):
        index = 0
        for i in range(0, len(self.alfabeto)):
            if(self.alfabeto[i] == simbolo):
                index = i
        return index

    def addRelacion(self, nodoinicial, nodofinal, simbolo):
        posAlfabeto = self.alfabetoindex(simbolo)
        self.tabla[nodoinicial][posAlfabeto].append(nodofinal)

    def sortRelaciones(self):
        for i in range(len(self.tabla)):
            for j in range(len(self.tabla[i])):
                self.tabla[i][j].sort()

    def Mostrar(self):

        print("Estado inicial: 0")
          
        print("Estados finales: ", end='')
        for i in range(0, len(self.EstadoFinal)):
            if(self.EstadoFinal[i] == True):
                print(i, "", end='')
        print("")

        print("Δ ", end='')
        for i in range(0, len(self.alfabeto)):
            print(self.alfabeto[i], "", end='')
        print("")
        for i in range(0, len(self.tabla)):
            print(i, "", end='')
            for j in range(len(self.alfabeto)):
                if(len(self.tabla[i][j]) == 0):
                    print("∅ ", end='')
                else:
                    print(self.tabla[i][j], "",end='')
            print("")
        print("\n")
        
