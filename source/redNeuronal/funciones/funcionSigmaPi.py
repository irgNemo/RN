#!/usr/bin/env python

from types import *

class FuncionSigmaPi(object):
	
	def calcular(self, vectorEntrada, pesos):
		resultado = 0.0
		if len(pesos) == len(vectorEntrada):
			for index in vectorEntrada:
				if type(vectorEntrada) is DictType:
					entrada = float(vectorEntrada[index])
				elif type(vectorEntrada) is ListType:
					entrada = float(index.salida)
				resultado = resultado + (entrada * pesos[index])
		else:
			print "La dimension del vector de entrada y de los pesos no son iguales"
		return resultado
