#!/usr/bin/python3
# -*- coding: utf-8 -*-

import sys


class Calculadora():

    def plus(self, Operando1, Operando2):
        return Operando1 + Operando2

    def minus(self, Operando1, Operando2):
        return Operando1 - Operando2


if __name__ == '__main__':

    Calc = Calculadora()

    try:
        Op1 = int(sys.argv[1])
        Op2 = int(sys.argv[3])
    except ValueError:
        sys.exit("Error: Non numerical arguments")

    Operacion = sys.argv[2]

    if Operacion == "plus":
        result = Calc.plus(Op1, Op2)
    elif Operacion == "minus":
        result = Calc.minus(Op1, Op2)
    else:
        sys.exit("I can only plus or minus")

    print(result)
