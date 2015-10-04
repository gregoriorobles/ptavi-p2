#!/usr/bin/python3
# -*- coding: utf-8 -*-
import sys
# Vamos a programar una calculadora

def main():
	pass

try :
	if sys.argv[2] == "sumar":
		main()
		a = int(sys.argv[1]);
		b = int(sys.argv[3]);
		print(a + b); 

	if sys.argv[2] == "restar":
		main()
		a = int(sys.argv[1]);
		b = -int(sys.argv[3]);
		print(a + b); 

	if sys.argv[2] == "dividir":
		main()
		a = int(sys.argv[1]);
		b = int(sys.argv[3]);
		try:
			print(a / b); 
		except ZeroDivisionError:
			print("Infinito");

	if sys.argv[2] == "multiplicar":
		main()
		a = int(sys.argv[1]);
		b = int(sys.argv[3]);
		print(a * b); 

except ValueError:
	print("Datos invalidos");
	

