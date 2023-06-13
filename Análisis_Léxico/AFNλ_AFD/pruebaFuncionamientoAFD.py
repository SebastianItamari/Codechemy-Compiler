from afd import *
automata = AFD(4, ["a", "b"], [2, 3])
automata.Mostrar()

automata.addRelacion(0, 2, "a")
automata.addRelacion(0, 1, "b")
automata.addRelacion(1, 2, "a")
automata.addRelacion(1, 3, "b")

automata.Mostrar()