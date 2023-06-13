from afn import *
from afnlambda import *
from conversiones import *
from conversionAFNAFD import *
from afd import *

#insertar automata 
automatainicial = AFNLambda(8, ["e", "l", "s"], [1])
automatainicial.addRelacion(0, 2, "λ")
automatainicial.addRelacion(0, 5, "λ")
automatainicial.addRelacion(2, 3, "e")
automatainicial.addRelacion(3, 4, "l")
automatainicial.addRelacion(4, 1, "λ")
automatainicial.addRelacion(5, 6, "e")
automatainicial.addRelacion(6, 7, "s")
automatainicial.addRelacion(7, 1, "λ")
print("\nAFN-λ")
automatainicial.Mostrar()

automataAFN = AFNLambdaAFN(automatainicial)
print("\nAFN")
automataAFN.Mostrar()

automataAFD = AFNtoAFD(automataAFN)
print("\nAFD")
automataAFD.Mostrar()


