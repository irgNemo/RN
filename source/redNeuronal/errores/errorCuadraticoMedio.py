#!/usr/bin/env python

class ErrorCuadraticoMedio(object):

	def __int__(self):
		self.error = None

	def calcularFuncion(self, correct, salida):
		return ( 0.5 * ((correct - salida)**2))

	def calcularDerivada(self, correct, salida):
		return correct - salida
