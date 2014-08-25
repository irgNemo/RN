#!/usr/bin/env python
from random import uniform

class Neurona(object):

	def __init__(self, funcionActivacion, funcionTransferencia):
		self.pesos = {}
		self.salida = 0
		self.entradas = [] 
		self.delta = 0
		self.funcionActivacion = funcionActivacion
		self.funcionTransferencia = funcionTransferencia
		self.neuronasSiguientes = []


	def funcionTransferencia(self, vectorEntrada, pesos):
		return self.funcionTransferencia.calcular(vectorEntrada, pesos)	

	def funcionActivacion(self, x):
		return self.funcionActivacion.calcularFuncion(x) 

	def crearVectorEntrada(self):
		return self.entradas 

	def calcular(self):
		if len(self.pesos) > 0:
			x = self.funcionTransferencia.calcular(self.entradas, self.pesos)
			self.salida = self.funcionActivacion.calcularFuncion(x)
			return self.salida
		else:
			# Lanzar una excepcion ya que la longitud de los pesos y el vector de entrada no es igual
			return None
