from afn import *
from afnlambda import *
from conversiones import *

automata = AFNLambda(5, ["a", "b"], [2,4])
automata.Mostrar()
automata.addRelacion(0, 1, "a")
automata.addRelacion(0, 3, "λ")
automata.addRelacion(1, 2, "λ")
automata.addRelacion(3, 3, "b")
automata.addRelacion(3, 4, "λ")
automata.addRelacion(4, 4, "a")
automata.Mostrar()
print("\n")
nuevoautomata = AFNLambdaAFN(automata)
nuevoautomata.Mostrar()