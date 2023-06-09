from afn import *
from afd import *

def ListasIguales(lista1, lista2):
    #menor se volvera lista1, mayor lista2
    
    listasIguales = True 
    if(len(lista1)!=len(lista2)):
        listasIguales = False 
    else:
        if(len(lista1)>len(lista2)):
            listamenor = lista2
            lista2 = lista1
            lista1 = listamenor 
        for i in range(0, len(lista1)):
            if(lista1[i]!=lista2[i]):
                listasIguales = False 
    return listasIguales


def AFNtoAFD(afn):
    #crear nuevas tablas
    nuevasRelaciones = []
    nuevosEstadoFinal = []
    equivalenciasEstados = []
    for i in range(0, len(afn.tabla)):
        nuevasRelaciones.append([])
        for j in range(0, len(afn.alfabeto)):
            nuevasRelaciones[i].append([])
        nuevosEstadoFinal.append(afn.EstadoFinal[i])
        equivalenciasEstados.append([])
        equivalenciasEstados[i].append(i)
    #llenar con datos de afn
    for i in range(0, len(afn.tabla)):
        for j in range(0, len(afn.tabla[i])):
            for k in range(0, len(afn.tabla[i][j])):
                nuevasRelaciones[i][j].append(afn.tabla[i][j][k])
            nuevasRelaciones[i][j].sort()

    #actualizar cada estado nuevo creado
    inicio = 0
    fin = len(nuevasRelaciones)
    #crear nuevos estados 
    while(inicio < fin):
        i = inicio 
        for j in range(0, len(nuevasRelaciones[i])):
            if(len(nuevasRelaciones[i][j]) > 1 and len(nuevasRelaciones[i][j]) != 0):
                #revisar si existe en equivalencias si if yes:
                foundinCurrentStates = False 
                for k in range(0, len(equivalenciasEstados)):
                    if(ListasIguales(nuevasRelaciones[i][j], equivalenciasEstados[k])==True):
                        #actualizar con estado nuevasRelaciones
                        #nuevasRelaciones[i][j] = [equivalenciasEstados[k]]
                        foundinCurrentStates = True 
                        break 
                if(foundinCurrentStates == False):
                    #if not crear nuevo estado
                    equivalenciasEstados.append(nuevasRelaciones[i][j])
                    #nuevasRelaciones[i][j] = [len(equivalenciasEstados)-1]
                    #crear tablas para nuevo estado
                    nuevasRelaciones.append([])
                    posNuevoEstado = len(nuevasRelaciones)-1
                    for l in range(0, len(afn.alfabeto)):
                        nuevasRelaciones[posNuevoEstado].append([])
                    #llenar tablas del nuevo estado
                    for x in range(0, len(afn.alfabeto)):
                        for y in range(0, len(equivalenciasEstados[posNuevoEstado])):
                            for z in range(0, len(nuevasRelaciones[equivalenciasEstados[posNuevoEstado][y]][x])):
                                if(nuevasRelaciones[equivalenciasEstados[posNuevoEstado][y]][x][z] not in nuevasRelaciones[posNuevoEstado][x]):
                                    nuevasRelaciones[posNuevoEstado][x].append(nuevasRelaciones[equivalenciasEstados[posNuevoEstado][y]][x][z])
                        nuevasRelaciones[posNuevoEstado][x].sort()        
        inicio = inicio + 1
        fin = len(nuevasRelaciones)

    #print(nuevasRelaciones)
    #print(len(nuevasRelaciones))

    #renombrar los estados con sus equivalencias y crear AFD
    for i in range(0, len(nuevasRelaciones)):
        for j in range(0, len(nuevasRelaciones[i])):
            if(len(nuevasRelaciones[i][j])>1):
                for k in range(0, len(equivalenciasEstados)):
                    if(ListasIguales(nuevasRelaciones[i][j], equivalenciasEstados[k]) == True):
                        nuevasRelaciones[i][j] = [k]
                        break 
    #print(nuevasRelaciones)

    #crear AFD
    nuevoAFD = AFD(len(nuevasRelaciones), afn.alfabeto, [])
    #crear nuevos estados finales
    for i in range(0, len(afn.EstadoFinal)):
        nuevoAFD.EstadoFinal[i] = afn.EstadoFinal[i] 
    for i in range(len(afn.tabla), len(nuevasRelaciones)):
        estadoesEstadoFinal = False
        for j in range(0, len(equivalenciasEstados[i])):
            if(afn.EstadoFinal[equivalenciasEstados[i][j]] == True):
                estadoesEstadoFinal = True 
                break 
        nuevoAFD.EstadoFinal[i] = estadoesEstadoFinal
    #print(nuevoAFD.EstadoFinal)

    #añadir relaciones de nuevasRelaciones
    nuevoAFD.tabla = nuevasRelaciones

    return nuevoAFD


