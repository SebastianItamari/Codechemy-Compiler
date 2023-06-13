from afnlambda import *
automata = AFNLambda(9, ["a", "b"], [2, 6, 8])
automata.Mostrar()

automata.addRelacion(0, 1, "λ")
automata.addRelacion(0, 3, "λ")
automata.addRelacion(0, 7, "λ")
automata.addRelacion(1, 2, "a")
automata.addRelacion(3, 3, "b")
automata.addRelacion(3, 4, "λ")
automata.addRelacion(4, 5, "a")
automata.addRelacion(5, 6, "b")
automata.addRelacion(7, 7, "a")
automata.addRelacion(7, 8, "λ")

automata.Mostrar()