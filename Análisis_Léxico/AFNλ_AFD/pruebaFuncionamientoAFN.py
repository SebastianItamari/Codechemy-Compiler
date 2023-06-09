#prueba funcionamiento afn
from afn import *
alfabeto = ["a", "b"]
automata = AFN(3, alfabeto, [2])
automata.Mostrar()

automata.addRelacion(0, 1, "b")
automata.addRelacion(1, 1, "a")
automata.addRelacion(1, 2, "a")
automata.addRelacion(1, 0, "b")
automata.addRelacion(2, 1, "b")
automata.addRelacion(2, 0, "a")

automata.Mostrar()