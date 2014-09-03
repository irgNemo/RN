#/usr/bin/env python
from neurona import Neurona
import re
from random import uniform
from types import *
from funciones import FuncionIdentidad 
import sys

class RedNeuronal(object):

	def __init__(self, funcionError, algoritmoAprendizaje, funcionActivacion, funcionTransferencia):
		self.capas =  None # Capas de neuronas
		self.conexiones = None # Conexiones entre capas
		self.algoritmoAprendizaje = algoritmoAprendizaje# Algoritmo de aprendizaje
		self.funcionError = funcionError 
		self.funcionActivacion = funcionActivacion
		self.funcionTransferencia = funcionTransferencia
		self.vectorErrorGlobal = []

	def crearCapas(self, neuronasPorCapa, conexiones):
		"""Crea las capas de la red Neuronal
		   Parametros:
		   	neuronaPorCapa: arreglo unidimensional con el numero de neuronas por capa. La dimension del vector indica las capas de la red neuronal. No se toma en cuenta la capa de entrada como capa de la red.
			rangosInicializacionPesos: los rangos de inicializacion para cada capa
			Return :regresa un arreglo bidimiensional con todas las neuronas necesarias en la red
		"""
		self.capas = []
		for i in xrange(len(neuronasPorCapa)):
			neuronas = []
			if i == 0:
				for j in xrange(int(neuronasPorCapa[i])):
					neurona = Neurona(FuncionIdentidad(), self.funcionTransferencia) 
					neuronas.append(neurona)
			else:			
				for j in xrange(int(neuronasPorCapa[i])):
					neurona = Neurona(self.funcionActivacion, self.funcionTransferencia)
					for conexion in conexiones[i]:
						if conexion[1] == j:
							neurona.entradas.append(self.capas[i - 1][conexion[0]])
							self.capas[i - 1][conexion[0]].neuronasSiguientes.append(neurona)
					neuronas.append(neurona)
			
			self.capas.append(neuronas)
		return self.capas

	def crearConexiones(self, conexiones):
		"""Crea o define las conexiones entre las neuronas en las respectivas capas.
		Parametros:
			conexiones: Indicar con la cadena FULL que representa una conexion completa de la red neuronal o una lista de tuplas correspondientes a las conexiones.
		return: Regresa un arreglo bidimensional con las conexiones en forma de tuplas
		"""
		if type(conexiones) is ListType:
			conjuntosConexiones = self.crearConexionesCompletas(conexiones)			
		elif type(conexiones) is StringType:
			conjuntosConexiones = self.extraerConexiones(conexiones)
		
		self.conexiones = conjuntosConexiones
		return self.conexiones

	def extraerConexiones(self, conexiones):
		"""Crea un arreglo bidimensional con las conexiones por cada capa de la red neuronal
		Parametro: Cadena con las conexiones como cadena de caracteres y en el formato especificado "[()()()()...()][()()()...()]...[()()()...()]"
		return un arreglo bidimensional con la informacion de las conexiones entre las capas de la red
		"""
		#Agregar un borrado de espacios en blanco en la cadena de entrada "conexiones"
		conexiones = self.quitarEspaciosEnBlanco(conexiones)
		patronSeparadorConjuntos = re.compile("(\[(\(\d+,\d+\))+\])")
		patronSeparadorTuplas =  re.compile("\(\d+,\d+\)")
		conjuntosConexiones = patronSeparadorConjuntos.findall(conexiones)
		conexionesTuplas = []
		for i in conjuntosConexiones:
			conjunto = i[0]	
			paresConjunto = patronSeparadorTuplas.findall(conjunto)
			tuplasSet = []
			for j in paresConjunto:
				tupla = tuple((int(v) - 1) for v in re.findall("[0-9]+", j))
				tuplasSet.append(tupla)	
			conexionesTuplas.append(tuplasSet)
		return conexionesTuplas

	def quitarEspaciosEnBlanco(self, conexiones):
		patron = re.compile('\s+')
		patron.sub('', conexiones)	
		return conexiones	

	def crearConexionesCompletas(self, dimensionCapas):
		"""Crea un arreglo con el conjunto de tuplas entre las neurona i y j en cada una de las capas de la red neuronal, la conexion es completa (FULL).
		"""
		conexiones = []
		for i in xrange(len(dimensionCapas)):
			if i == 0:
				conjuntoTuplas = [] 
				for j in xrange(int(dimensionCapas[i])):
					conjuntoTuplas.append((j,j))
				conexiones.append(conjuntoTuplas)		
						
			if (i + 1) < len(dimensionCapas):
				conjuntoTuplas = [] 
				for j in xrange(int(dimensionCapas[i])):
					for k in xrange(int(dimensionCapas[i + 1])):
						conjuntoTuplas.append((j,k))
				conexiones.append(conjuntoTuplas)
		return conexiones

	def inicializarPesos(self, capas, conexiones, rangosInicializacionPesos):
		"""Inicializa los pesos de las neuronas en cada capa, de acuerdo con el rango de cada capa
		Parametros:
			capas: arreglo bidimiensional con las neuronas por capa
			conexiones: arreglo bidimiensional con las conexiones por capa.
			rangoInicializacionPesos: arreglo bidimensional con los rangos de inicializacion por cada capa.
		"""

		rangosInicializacionPesos = self.extraerRangosInicializacionPesos(rangosInicializacionPesos)
		for i in xrange(0, len(conexiones)):
			for j in xrange(len(conexiones[i])):
				tupla = conexiones[i][j] 
				neurona = capas[i][tupla[1]]
				if i == 0:
					neurona.pesos[tupla[1]] = 1 
				else:
					rangoInicial = rangosInicializacionPesos[i][0]
					rangoFinal = rangosInicializacionPesos[i][1]
					neurona.pesos[capas[i - 1][tupla[0]]] = uniform(float(rangoInicial), float(rangoFinal))

	def extraerRangosInicializacionPesos(self, rangosString):
		listaTuplas = []
		#Agregar un remplazo de espacio en blanco por nada entre la cadena de entrada rangosString
		patronRangos = re.compile("\[-?[0-9.]+,-?[0-9.]+\]")
		rangos = patronRangos.findall(rangosString) 
		for i in rangos:
			tupla = tuple(float(v) for v in re.findall("[0-9.-]+", i))
			listaTuplas.append(tupla)
		return listaTuplas
	
	def aprender(self, instancias, iteraciones):
		for iteracion in xrange(iteraciones):
			#print "---------- Iteracion " + str(iteracion) + " --------------"
			i = 0
			for instancia in instancias:
				if i == 0:
					print instancia.clase
				#print "----------- Instancia " + str(i) + "-----------"
				if type(instancia.vectorSalidaEsperado) is ListType:
					self.asociarNeuronaSalidaConClaseInstancia(self.capas[len(self.capas) - 1], instancia)
				self.propagarHaciaAdelante(self.capas, instancia)	
				self.propagacionHaciaAtras(self.capas, instancia, 0.2)
				i = i + 1
				if len(self.vectorErrorGlobal) == 0:
					self.vectorErrorGlobal = [sys.maxint] * len(instancia.vectorSalidaEsperado)
				indiceUltimaCapa = len(self.capas) - 1
				for indice in xrange(len(self.capas[indiceUltimaCapa])):
					neurona = self.capas[indiceUltimaCapa][indice]
					self.vectorErrorGlobal[indice] = neurona.salida	
				print str(self.vectorErrorGlobal)  

	def propagarHaciaAdelante(self, capas, instancia):
		vectorErrores = {}
		for indiceCapa in xrange(len(capas)):
		    for indiceNeurona in xrange(len(capas[indiceCapa])):
			    neurona = capas[indiceCapa][indiceNeurona]
			    if indiceCapa == 0:
				    if type(neurona.entradas) is ListType:
			                del neurona.entradas[:]
				    elif type(neurona.entradas) is DictType:
					    neurona.entradas.clear()
				    neurona.entradas = {indiceNeurona: instancia.atributos[indiceNeurona]}
			    neurona.calcular()

	def propagacionHaciaAtras(self, capas, instancia, razonAprendizaje):
		for indiceCapa in xrange(len(capas) - 1, 0 , -1):
			esCapaSalida = True if (indiceCapa == (len(capas) - 1)) else False
			#print "----- Capa " + str(indiceCapa) + " ---------"
			for neurona in capas[indiceCapa]:
				#print "Antes: " + str(neurona.pesos)
				self.algoritmoAprendizaje.calcularNuevosPesos(neurona, instancia, razonAprendizaje, esCapaSalida)
				#print "Despues: " + str(neurona.pesos)
	# Esta funcion asocia las salidas de la red neuronal con los correpondientes valores esperados de acuerdo con las instancias
	def asociarNeuronaSalidaConClaseInstancia(self, capaFinal, instancia):
		relacionNeuronaVectorSalidaEsperado = {}
		i = 0
		for neuronaFinal in capaFinal:
			relacionNeuronaVectorSalidaEsperado[neuronaFinal] = instancia.vectorSalidaEsperado[i]
			i = i + 1
		instancia.vectorSalidaEsperado = relacionNeuronaVectorSalidaEsperado
