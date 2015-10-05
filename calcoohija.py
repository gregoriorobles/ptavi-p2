#!/usr/bin/python3
# -*- coding: utf-8 -*-

import sys
import calcoo


class CalculadoraHija (calcoo.Calculadora):

    def product(self, Operando1, Operando2):
        return Operando1*Operando2

    def divide(self, Operando1, Operando2):
        return Operando1/Operando2


if __name__ == '__main__':

    CalcHija = CalculadoraHija()

    try:
        Op1 = int(sys.argv[1])
        Op2 = int(sys.argv[3])
    except ValueError:
        sys.exit("Error: Non numerical arguments")

    Operate = sys.argv[2]

    if Operate == "suma":
        result = CalcHija.plus(Op1, Op2)
    elif Operate == "resta":
        result = CalcHija.minus(Op1, Op2)
    elif Operate == "multiplicacion":
        result = CalcHija.product(Op1, Op2)
    elif Operate == "division":
        try:
            result = CalcHija.divide(Op1, Op2)
        except ZeroDivisionError:
            sys.exit('Division by zero is not allowed')
    else:
        sys.exit('Possible operations: /suma/resta/division/multiplicacion/')

    print(result)
