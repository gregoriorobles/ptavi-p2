#!/usr/bin/python3
# -*- coding: utf-8 -*-

import sys

from calcoohija import CalculadoraHija

ddp = CalculadoraHija()

if __name__ == "__main__":

	fich = open(sys.argv[1],'r')
	lines = fich.readlines()

for line in lines:
	trozo=line.split(',')
	resultado=int(trozo[1])

	if (line[:line.find(',')]) == "suma":
		for n in range(2,len(trozo)):
			resultado = ddp.plus(resultado, int(trozo[n]))
		print(resultado)

	elif (line[:line.find(',')]) == "resta":
		for n in range(2,len(trozo)):
			resultado = ddp.minus(resultado, int(trozo[n]))
		print(resultado)

	elif (line[:line.find(',')]) == "multiplica":
		for n in range(2,len(trozo)):
			resultado = ddp.mult(resultado, int(trozo[n]))
		print(resultado)
	
	elif (line[:line.find(',')]) == "divide":
		for n in range(2,len(trozo)):
			if int(trozo[n]) != 0:
				resultado = ddp.divide(resultado, int(trozo[n]))
			else:
				sys.exit("Error: Division by zero is not allowed")
	
		print(resultado)
		
	else:
		print ("La operacion no es valida para nuestra calculadora.")
	
