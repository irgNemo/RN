#!/usr/bin/env python
import math

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
		#		estaditicas = validacionEstratificada(modelo, conjuntoDatos)
		#		estadisticasPorKfold[kfold] = estadisticas
		#		kfold = kfold - 1
		#	estadisticasPorRepeticiones[self.repeticionesKfold] = estadisticasPorKfold
		#self.repeticionesKfold = self.repeticionesKfold - 1
		#imprimitEstadisticas(estadisticasPorRepeticiones)


	def separarConjuntosDatos(self, instanciasEntrenamiento, kfold):
		entrenamiento = []
		validacion = []
		clases = {}
		elementosPorParticion = len(instanciasEntrenamiento) / kfold
		for instancia in instanciasEntrenamiento:
			if clases.has_key(instancia.clase) == False:
				clases[instancia.clase] = []
			clases[instancia.clase] = instancia
		instanciasParaValidacionPorClase = math.ceil(elementosPorParticion / len(clases))
		for clase in clases:
			print clases[clase]

