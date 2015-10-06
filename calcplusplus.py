#!/usr/bin/python3
# -*- coding: utf-8 -*-

import sys

import csv

from calcoohija import CalculadoraHija

ddp = CalculadoraHija()

with open(sys.argv[1],'r') as d
	lines = csv.lines(d)

	for row in lines:
		trozo=row.split(',')
		resultado=int(trozo[1])

		if (row[:row.find(',')]) == "suma":
			
			for n in range(2,len(trozo)):
				resultado = ddp.plus(resultado, int(trozo[n]))
			print(resultado)

		elif (row[:row.find(',')]) == "resta":
			
			for n in range(2,len(trozo)):
				trozo=row.split(',')
				resultado = ddp.minus(resultado, int(trozo[n]))
			print(resultado)

		elif (row[:row.find(',')]) == "multiplica":

			for n in range(2,len(trozo)):
				trozo=row.split(',')
				resultado = ddp.mult(resultado, int(trozo[n]))
			print(resultado)
	
		elif (row[:row.find(',')]) == "divide":

			for n in range(2,len(trozo)):
				trozo=row.split(',')
				if int(trozo[n]) != 0:
					resultado = ddp.divide(resultado, int(trozo[n]))
				else:
					sys.exit("Error: Division by zero is not allowed")
	
			print(resultado)
		
		else:
			print ("La operacion no es valida para nuestra calculadora.")
	
