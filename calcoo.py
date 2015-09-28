#!/usr/bin/python3
# -*- coding: utf-8 -*-

import sys

def plus(op1, op2):
    """ Function to sum the operands """
    return op1 + op2


def minus(op1, op2):
    """ Function to substract the operands """
    return op1 - op2

class Calculadora(self, suma, resta):
    self.suma= plus
    self.resta= minus

if __name__ == "__main__":
    try:
        operando1 = int(sys.argv[1])
        operando2 = int(sys.argv[3])
        operacion = int(sys.argv[2])
    
    if sys.argv[2] == "suma":
        return Calculadora.suma
    elif sys.arg[2] == "resta":
        return Calculadora.resta
    else
        "Operaciones validas SUMAS O RESTAS"

    print (Calculadora)
    
