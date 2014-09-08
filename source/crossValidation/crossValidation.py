#!/usr/bin/env python
import math
import random

class CrossValidation(object):
	def __init__(self, modelo, kfold, repeticionesKfold, instanciasEntrenamiento):
		self.kfold = kfold
		self.modelo = modelo
		self.instanciasEntrenamiento = instanciasEntrenamiento
		self.repeticionesKfold = repeticionesKfold

	def ejecutar(self):
		#estadisticasPorRepeticiones = {}
		#kfold = self.kfold
		#while self.repeticionesKfold > 0:
		#	estadisticasPorKfold = {} 
		#	while kfold > 0:
				conjuntosDatos = self.separarConjuntosDatos(self.instanciasEntrenamiento, self.kfold)
				resultados = self.validacionEstratificada(self.modelo, conjuntosDatos)
				for instancia in conjuntosDatos["validacion"]:
					print str(instancia.vectorSalidaEsperado) + ":" + str(resultados[instancia]) 
		#		estadisticasPorKfold[kfold] = resultados 
		#		kfold = kfold - 1
		#	estadisticasPorRepeticiones[self.repeticionesKfold] = estadisticasPorKfold
		#self.repeticionesKfold = self.repeticionesKfold - 1
		#imprimitEstadisticas(estadisticasPorRepeticiones)

	def validacionEstratificada(self, modelo, conjuntoDatos):
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

