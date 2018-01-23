#!/usr/bin/env python
from instancia import Instancia

class CargarBaseDeDatos(object):

	def leerArchivo(self, ruta, separador, posicionClase, valoresEsperadosPorClase):
		archivoEntrada = open(ruta, "r")
		instancias = []
		atributos = []
		clase = ""
		for linea in archivoEntrada:
			linea = linea.strip()
			linea = linea.split(separador)
			if len(linea) < len(valoresEsperadosPorClase):
				continue
			for i in xrange(len(linea)):
				if i == (posicionClase - 1):
					clase = linea[i]
				else:
					atributos.append(linea[i])
			atributos.append(1) # Se agrega para ser el bias de la red neuronal
			instancias.append(Instancia(atributos, clase, valoresEsperadosPorClase[clase]))	
			atributos = []
		archivoEntrada.close()
		return instancias


"""
if __name__ == "__main__":
	cargarBase = CargarBaseDeDatos()
	instancias = cargarBase.leerArchivo("iris.data",",",5,{"Iris-setosa":[1,-1,-1], "Iris-versicolor":[-1,1,-1], "Iris-virginica":[-1,-1,1]})
	for instancia in instancias:
		print str(instancia.atributos) + ":" + instancia.clase
"""	
