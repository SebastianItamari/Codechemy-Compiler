from conversionAFNAFD import *
from afd import *
from afn import *

class ConversionAFNaAFD:
    def __init__(self):
        self.afn = 0
        self.afd = 0
    def crearAFN(self):
        print("CREAR AFN")
        print("Ingresar el alfabeto del autómata: ", end='')
        alfabeto = input().split()
        print("Ingresar el número de estados del autómata: ", end='')
        numeroEstados = int(input())
        print("Ingresar los estados finales: ", end='')
        estadosfinales = input().split()
        for i in range(0, len(estadosfinales)):
            estadosfinales[i] = int(estadosfinales[i]) 
        self.afn = AFN(numeroEstados, alfabeto, estadosfinales)
        print("\n")
    
    def crearCambiosdeEstado(self):
        print("AÑADIR MÚLTIPLES CAMBIOS DE ESTADO")
        print("Ingresar el número de cambios de estados a añadir: ", end='')
        numeroCambios = int(input())
        for i in range(0, numeroCambios):
            self.crearCambiodeEstado()
        self.afn.sortRelaciones()

    def crearCambiodeEstado(self):
        print("AÑADIR CAMBIO DE ESTADO AL AFN")
        print("Ingresar primer estado: ", end='')
        primerestado = int(input())
        print("Ingresar estado al que se cambiará: ", end='')
        segundoestado = int(input())
        print("Símbolo para el cambio de estado: ", end='')
        simbolo = input()
        self.afn.addRelacion(primerestado, segundoestado, simbolo)
        print("\n")
        

    def MostrarAFN(self):
        self.afn.Mostrar()
        print("\n")

    def MostrarAFD(self):
        self.afd.Mostrar()
        print("\n")

    def ConvertirAFNaAFD(self):
        self.afd = AFNtoAFD(self.afn)



