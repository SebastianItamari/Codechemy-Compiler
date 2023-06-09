from conversionAFNAFD import *
from afn import *
from afd import *

automataAFN = AFN(4, ["a", "b"], [3])
automataAFN.addRelacion(0, 0, "a")
automataAFN.addRelacion(0, 1, "a")
automataAFN.addRelacion(0, 2, "a")
automataAFN.addRelacion(1, 2, "a")
automataAFN.addRelacion(1, 1, "b")
automataAFN.addRelacion(1, 3, "b")
automataAFN.addRelacion(2, 3, "a")
automataAFN.addRelacion(3, 3, "a")
automataAFN.addRelacion(3, 2, "b")
automataAFN.addRelacion(3, 3, "b")
print("AFN")
automataAFN.Mostrar()
automataAFD = AFNtoAFD(automataAFN)
print("\nAFD")
automataAFD.Mostrar()



