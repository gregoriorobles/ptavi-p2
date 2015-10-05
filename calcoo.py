#!/usr/bin/python3
# -*- coding: utf-8 -*-

import sys


class Calculadora():

    def check(self, op1, op2):
        try:
            op1 = float(op1)
            op2 = float(op2)
        except ValueError:
            sys.exit("Error: Non numerical parameters")
        return (op1, op2)

    def suma(self, op1, op2):
        op1, op2 = self.check(op1, op2)
        return op1 + op2

    def resta(self, op1, op2):
        op1, op2 = self.check(op1, op2)
        return op1 - op2

if __name__ == "__main__":
    operando1 = sys.argv[1]
    operando2 = sys.argv[3]
    operacion = sys.argv[2]

    calcu = Calculadora()
    if operacion == "suma":
        resultado = calcu.suma(operando1, operando2)
    elif operacion == "resta":
        resultado = calcu.resta(operando1, operando2)
    else:
        print("Operaciones validas SUMAS O RESTAS")

    print (resultado)
