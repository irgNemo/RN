#!/usr/bin/env pyhton

class EstadisticaValidacionCruzada(object):
	def __init__(self):
		self.matrizConfusion = {} 

	def agregarResultado(self, vectorClaseEsperada, vectorClaseResultado):
		if len(vectorClaseEsperada) != len(vectorClaseResultado) or len(vectorClaseEsperada) == 0 or len(vectorClaseResultado) == 0:
			print "Dimension de vectores diferente o igual a 0"
			return
		for neuronaClaseEsperada in vectorClaseEsperada.keys():
			vectorTemporal = self.matrizConfusion[neuronaClaseEsperada] if self.matrizConfusion.has_key(neuronaClaseEsperada) else {}
			for neuronaClaseResultado in vectorClaseResultado.keys():
				if not vectorTemporal.has_key(neuronaClaseResultado):
					vectorTemporal[neuronaClaseResultado] = 0
				if vectorClaseEsperada[neuronaClaseEsperada] == 1 and vectorClaseResultado[neuronaClaseResultado] == 1:
					vectorTemporal[neuronaClaseResultado] = vectorTemporal[neuronaClaseResultado] + 1
			self.matrizConfusion[neuronaClaseEsperada] = vectorTemporal
		
	def imprimirMatrizConfusion(self):
		for fila in self.matrizConfusion.keys():
			print ''.join(str(self.matrizConfusion[fila].values()))
