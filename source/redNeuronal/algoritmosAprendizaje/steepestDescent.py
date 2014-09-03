#!/usr/bin/env python

class SteepestDescent(object):
	
	def __init__(self, funcionError, funcionActivacion, funcionTransferencia):
		self.funcionError = funcionError 
		self.funcionActivacion = funcionActivacion
		self.funcionTransferencia = funcionTransferencia

	def calcularDeDy(self, salidaRed, salidaEsperada):
		return self.funcionError.calcularDerivada(salidaEsperada, salidaRed)

	def calcularDyDnet(self, salidaRed):
		return self.funcionActivacion.calcularDerivada(salidaRed)

	def calcularNuevosPesos(self, neurona, instancia, razonAprendizaje, esCapaSalida):
		if esCapaSalida: 
			DyDnet = self.calcularDyDnet(neurona.salida)
			DeDy = self.calcularDeDy(neurona.salida, instancia.vectorSalidaEsperado[neurona])
			delta = DeDy * DyDnet
			neurona.delta = delta
			for neuronaEntrada in neurona.entradas:
				deltaWk = razonAprendizaje * delta * neuronaEntrada.salida
				neurona.pesos[neuronaEntrada] = neurona.pesos[neuronaEntrada] + deltaWk
		else:
			DyDnet = self.calcularDyDnet(neurona.salida)
			sumatoria = 0
			for neuronaSiguiente in neurona.neuronasSiguientes:
				for neuronaLlave in neuronaSiguiente.pesos:
					if neuronaLlave == neurona:
						sumatoria = sumatoria + neuronaSiguiente.pesos[neurona] * neuronaSiguiente.delta
			delta = sumatoria * DyDnet
			neurona.delta = delta
			for neuronaEntrada in neurona.entradas:
				deltaWk = razonAprendizaje * delta * neuronaEntrada.salida
				neurona.pesos[neuronaEntrada] = neurona.pesos[neuronaEntrada] + deltaWk 
