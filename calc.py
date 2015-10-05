#!/usr/bin/python3
# -*- coding: utf-8 -*-

import sys


def suma(operando1, operando2):
    return operando1 + operando2


def resta(operando1, operando2):
    return operando1 - operando2

if __name__ == "__main__":
    try:
        operando1 = int(sys.argv[1])
        operacion = sys.argv[2]
        operando2 = int(sys.argv[3])
    except ValueError:
        sys.exit("Error: Non numerical parameters")

    if operacion == "suma":
        resultado = suma(operando1, operando2)
    elif operacion == "resta":
        resultado = resta(operando1, operando2)
    else:
        sys.exit("operacion no valida")

    print(resultado)
