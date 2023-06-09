from afd import *
from afn import * 
from afnlambda import *
def ValueinList(value, list):
    ans = False
    for i in range(0, len(list)):
        if(list[i] == value):
            ans = True 
    return ans 
def Combinarlistas(lista1, lista2):
    for i in range(0, len(lista2)):
        if(ValueinList(lista2[i], lista1) == False):
            lista1.append(lista2[i])
    return lista1
def ObtenerClausura(index, afnlambda):
    clausurasIndex = []
    clausurasIndex.append(index)
    poslambda = len(afnlambda.alfabeto)-1
    for j in range(0, len(afnlambda.tabla[index][poslambda])):
        newvalue = afnlambda.tabla[index][poslambda][j]
        if(ValueinList(newvalue, clausurasIndex) == False):
            clausurasIndex.append(newvalue)
            otraclausura = ObtenerClausura(newvalue, afnlambda)
            clausurasIndex = Combinarlistas(clausurasIndex, otraclausura)

    return clausurasIndex

def AFNLambdaAFN(afnlambda):
    numeroEstados = len(afnlambda.tabla)
    #region OBTENER CLAUSURA
    #obtener clausuras
    clausuras = []
    for i in range(0, numeroEstados):
        clausuras.append(ObtenerClausura(i, afnlambda))  
        
    #endregion

    for i in range(0, numeroEstados):
        print(i, ", clausura:", clausuras[i])
    print("\n")
    #crear nuevo alfabeto sin lambda
    nuevoalfabeto = []
    for i in range(0, len(afnlambda.alfabeto)-1):
        nuevoalfabeto.append(afnlambda.alfabeto[i])

    #crear nueva relacion para cada estado con cada letra del alfabeto
    nuevoautomata = AFN(numeroEstados, nuevoalfabeto, [0])
    nuevoautomata.EstadoFinal = afnlambda.EstadoFinal

    nuevoautomata.Mostrar()
    for i in range(0, numeroEstados): # i = q0
        for j in range(0, len(afnlambda.alfabeto)-1): #j = a
            #∆′(q0, a) = λ[∆(λ[q0], a)]
            delta = [] #∆(λ[q0], a)
            for k in range(0, len(clausuras[i])): #elemento de λ[q0]
                valordeclausuras = clausuras[i][k]
                for l in range(0, len(afnlambda.tabla[valordeclausuras][j])):
                    nuevovalor = afnlambda.tabla[valordeclausuras][j][l]
                    if(ValueinList(nuevovalor, delta) == False):
                        delta.append(nuevovalor )
            print("i =", i)
            print("alfabeto:", afnlambda.alfabeto[j])
            print(delta, "\n")
            #λ[∆]
            nuevarelacion = []
            for k in range(0, len(delta)):
                for l in range(0, len(clausuras[delta[k]])):
                    nuevovalorRelacion = clausuras[delta[k]][l]
                    if(ValueinList(nuevovalorRelacion, nuevarelacion) == False):
                        nuevarelacion.append(nuevovalorRelacion)

            for k in range(0, len(nuevarelacion)):
                nuevoautomata.addRelacion(i, nuevarelacion[k], afnlambda.alfabeto[j])
    return nuevoautomata     


