#!/usr/bin/env python
from math import exp

class FuncionSigmoidal(object):

	def calcularFuncion(self, x):
		return 1 / (1 + exp(-x))

	def calcularDerivada(self, x):
		return x * (1 - x)

