#!/usr/bin/python
##tablas multiplicar

rango = range(11)
cadena = "Tabla del "

for numero in rango[1:]:
	print("--------------")
	print(cadena + str(numero))
	for numero2 in rango[1:]:
		resultado = (numero * numero2)
		print(str(numero) + " * " + str(numero2) + " = " + str(resultado))

