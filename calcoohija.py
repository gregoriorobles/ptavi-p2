#!/usr/bin/python3
# -*- coding: utf-8 -*-

import sys
import calcoo

class CalculadoraHija (calcoo.Calculadora):
    def multiplica(self, op1, op2):
        return op1 * op2
    def divide (self, op1, op2):
        return op1 / op2 

if __name__ == "__main__":
    try:
        operando1 = float(sys.argv[1])
        operando2 = float(sys.argv[3])
        operacion = sys.argv[2]
    except ValueError:
        sys.exit("Error: Non numerical parameters")
    
    calcu = CalculadoraHija()

    if operacion == "suma":
        resultado = calcu.suma (operando1, operando2)
    elif operacion == "resta":
        resultado = calcu.resta (operando1, operando2)
    elif operacion == "multiplica":
        resultado = calcu.multiplica (operando1, operando2)
    elif operacion == "divide":
        if operando2 == 0:
            sys.exit("Division by zero is not allowed")
        else:
            resultado = calcu.divide (operando1, operando2)
    else:
        print("Operacion no valida")

    print(resultado)


            
    
