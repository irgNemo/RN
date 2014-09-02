#!/usr/bin/env python

from redNeuronal import RedNeuronal
from redNeuronal.errores import ErrorCuadraticoMedio
from redNeuronal.algoritmosAprendizaje import SteepestDescent
from redNeuronal.funciones import FuncionSigmoidal
from basesDatos.instancia import Instancia
from redNeuronal.funciones import FuncionSigmaPi


def main():
	#Siempre agregar al valor de las instancias el bias que se utilizara para la red neuronal
	instancias = [Instancia([1,2,3,4,5,1],'versicolor', [1,-1,-1]), Instancia([4,3,2,1,1,1], 'virginica', [-1,1,-1]), Instancia([4,5,8,9,7,1],"setosa",[-1,-1,1])]
	rangosInicializacionPesos = "[1,1][-0.5,0.5][-0.45,0.70]" #Los rangos para la inicializacion de los pesos para las neuronas de cada capa
	dimensionCapas = ['5','4','3'] #Dimension de las capas de la red neuronal, la primera corresponde siempre a la capa de entrada.
	conexiones = "[(1,1)(2,2)(3,3)(4,4)(5,5)][(1,1)(2,4)(1,3)(3,2)(4,4)][(1,1)(2,1)(3,2)(4,2)(2,3)(3,3)]" #Conexiones entre las neuronas de la red neuronal. El primero valor de la tupla es la neurona i de la capa emisora y el segundo valor de la tupla es el numero de la neurona de la capa receptora. La posicion en el arreglo de conexiones indica la capa a la que corresponde 

	funcionActivacion = FuncionSigmoidal()
	funcionTransferencia = FuncionSigmaPi()
	redNeuronal = RedNeuronal(ErrorCuadraticoMedio(), SteepestDescent(ErrorCuadraticoMedio(), funcionActivacion, funcionTransferencia), funcionActivacion, funcionTransferencia)
	conexionesList = redNeuronal.crearConexiones(conexiones)
	capas = redNeuronal.crearCapas(dimensionCapas, conexionesList)
	redNeuronal.inicializarPesos(capas, conexionesList, rangosInicializacionPesos)
	redNeuronal.aprender(instancias, 1000)	
	capaSalida = redNeuronal.capas[len(redNeuronal.capas) - 1]

if __name__ == "__main__":
	main()
