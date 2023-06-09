from afn import *
from afnlambda import *
from conversiones import *

automatainicial = AFNLambda(8, ["e", "l", "s"], [1])
automatainicial.addRelacion(0, 2, "λ")
automatainicial.addRelacion(0, 5, "λ")
automatainicial.addRelacion(2, 3, "e")
automatainicial.addRelacion(3, 4, "l")
automatainicial.addRelacion(4, 1, "λ")
automatainicial.addRelacion(5, 6, "e")
automatainicial.addRelacion(6, 7, "s")
automatainicial.addRelacion(7, 1, "λ")
automatainicial.Mostrar()

nuevoAFN = AFNLambdaAFN(automatainicial)
nuevoAFN.Mostrar()
