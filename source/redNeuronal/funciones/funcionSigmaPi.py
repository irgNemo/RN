#!/usr/bin/env python

from types import *

class FuncionSigmaPi(object):
	
	def calcular(self, vectorEntrada, pesos):
		resultado = 0
		if len(pesos) == len(vectorEntrada):
			for index in vectorEntrada:
				if type(vectorEntrada) is DictType:
					entrada = vectorEntrada[index]
				elif type(vectorEntrada) is ListType:
					entrada = index.salida
				resultado = resultado + (entrada * pesos[index])
		return resultado
