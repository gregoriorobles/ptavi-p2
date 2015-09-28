#!/usr/bin/python3
# -*- coding: utf-8 -*-

import sys



class Calculadora():
    def suma (self, op1, op2):
        return op1 + op2
    def resta (self, op1, op2):
        return op1 - op2

if __name__ == "__main__":
    try:
        operando1 = int(sys.argv[1])
        operando2 = int(sys.argv[3])
        operacion = sys.argv[2]
    
    calcu = Calculadora()
    if operacion == "suma":
        resultado = calcu.suma(operando1,operando2)
    elif operacion == "resta":
        resultado = calcu.resta(operando1,operando2)
    else
        print("Operaciones validas SUMAS O RESTAS")

    print (resultado)
    
