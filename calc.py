#!/usr/bin/python3
# -*- coding: utf-8 -*-

import sys

from calcoohija import CalculadoraHija

ddp = CalculadoraHija()

if __name__ == "__main__":
	
	try:
		operando1 = int(sys.argv[1])
		operando2 = int(sys.argv[3])
	except ValueError:
		sys.exit("Error: Non numerical parameters")

	if sys.argv[2] == "suma":
		result = ddp.plus(operando1, operando2)
	elif sys.argv[2] == "resta":
		result = ddp.minus(operando1, operando2)
	elif sys.argv[2] == "multiplica":
		result = ddp.mult(operando1, operando2)
	elif sys.argv[2] == "divide":
		if operando2 != 0:
			result = ddp.divide(operando1, operando2)
		else:
			sys.exit("Error: Division by zero is not allowed")
	else:
		sys.exit('Operación sólo puede ser sumar, restar, multiplicar 			o dividir')

	print(result)
