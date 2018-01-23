#!/usr/bin/env python
import math
import random
from estadisticaValidacionCruzada import EstadisticaValidacionCruzada

class CrossValidation(object):
	def __init__(self, modelo, kfold, repeticionesKfold, instanciasEntrenamiento):
		self.kfold = kfold
		self.modelo = modelo
		self.instanciasEntrenamiento = instanciasEntrenamiento
		self.repeticionesKfold = repeticionesKfold

	def ejecutar(self):
		estadisticasPorRepeticiones = {}
		repeticionesKfold = self.repeticionesKfold
		while repeticionesKfold > 0:
			print "Repeticiones KFold: " + str(repeticionesKfold) 
			estadisticasPorKfold = {} 
			kfold = self.kfold
			while kfold > 0:
				print "Kfold: " + str(kfold)
				conjuntosDatos = self.separarConjuntosDatos(self.instanciasEntrenamiento, self.kfold)
				resultados = self.validacionEstratificada(self.modelo, conjuntosDatos)
				estadisticaValidacionCruzada = None
				for instancia in conjuntosDatos["validacion"]:
					if estadisticaValidacionCruzada == None:
						estadisticaValidacionCruzada = EstadisticaValidacionCruzada()
					estadisticaValidacionCruzada.agregarResultado(instancia.vectorSalidaEsperado, resultados[instancia])
				estadisticasPorKfold[kfold] = estadisticaValidacionCruzada 
				kfold = kfold - 1
				estadisticaValidacionCruzada.imprimirMatrizConfusion()
			estadisticasPorRepeticiones[repeticionesKfold] = estadisticasPorKfold
			repeticionesKfold = repeticionesKfold - 1
		#imprimitEstadisticas(estadisticasPorRepeticiones)

	def validacionEstratificada(self, modelo, conjuntoDatos):
		modelo.inicializacion()
		modelo.aprender(conjuntoDatos["entrenamiento"])
		return modelo.recuperacion(conjuntoDatos["validacion"])


	def separarConjuntosDatos(self, instanciasEntrenamiento, kfold):
		entrenamiento = []
		validacion = []
		clases = {}
		instanciasPorParticion = len(instanciasEntrenamiento) / kfold
		for instancia in instanciasEntrenamiento:
			if clases.has_key(instancia.clase) == False:
				clases[instancia.clase] = []
			clases[instancia.clase].append(instancia)
		instanciasParaValidacionPorClase = int(math.ceil(instanciasPorParticion / len(clases)))
		for clase in clases:
			for i in xrange(instanciasParaValidacionPorClase):
				obj = random.choice(clases[clase])
				validacion.append(obj)
				clases[clase].remove(obj)
			entrenamiento.extend(clases[clase])
		return {"validacion":validacion, "entrenamiento":entrenamiento} 

