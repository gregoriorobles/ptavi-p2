#!/usr/bin/python3
# -*- coding: utf-8 -*-

import calcoo
import sys


class CalculadoraHija(calcoo.Calculadora):
    def multi(self, op1, op2):
        return op1 * op2

    def div(self, op1, op2):
        return op1 / op2


if __name__ == "__main__":
    calchija = CalculadoraHija()
    try:
        operando1 = int(sys.argv[1])
        operando2 = int(sys.argv[3])
    except:
        sys.exit("Error: Non numerical parameters")

    if sys.argv[2] == "suma":
        result = (calchija.plus(operando1, operando2))
    elif sys.argv[2] == "resta":
        result = (calchija.minus(operando1, operando2))
    elif sys.argv[2] == "multiplica":
        result = (calchija.multi(operando1, operando2))
    elif sys.argv[2] == "divide":
        try:
            result = (calchija.div(operando1, operando2))
        except:
            op2 = 0
            sys.exit("Division by zero is not allowed")
    else:
        sys.exit("Operación sólo puede ser sumar,restar, multiplicar o dividir")

    print(result)
