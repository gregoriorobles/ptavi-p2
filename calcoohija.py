#!/usr/bin/python3
# -*- coding: utf-8 -*-


import sys
import calcoo


class CalculadoraHija(calcoo.Calculadora):

    def producto(self, operando1, operando2):
        return (operando1 * operando2)

    def division(self, operando1, operando2):
        try:
            return(operando1 / operando2)
        except operando2 == 0:
             print("Division by zero is not allowed")

if __name__ == "__main__":

        calc = CalculadoraHija()

        try:
            operando1 = int(sys.argv[1])
            operacion = sys.argv[2]
            operando2 = int(sys.argv[3])
        except ValueError:
            sys.exit("Error: Non numerical parameters")

        if operacion == "suma":
            resultado = calc.suma(operando1, operando2)
        elif operacion == "resta":
            resultado = calc.resta(operando1, operando2)
        elif operacion == "multiplica":
            resultado = calc.producto(operando1, operando2)
        elif operacion == "divide":
            resultado = calc.division(operando1, operando2)
        else:
            sys.exit("operacion no valida")

        print(resultado)
