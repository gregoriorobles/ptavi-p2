#   ROBERTO YUBERO DE DIEGO
#!/usr/bin/python3
# -*- coding: utf-8 -*-

import sys


class Calculadora:

    def suma(self, op1, op2):
        """ Funcion suma"""
        return op1 + op2

    def resta(self, op1, op2):
        """ Funcion resta """
        return op1 - op2


if __name__ == "__main__":

    miCalculadora = Calculadora()
    try:
        operando1 = int(sys.argv[1])
        operando2 = int(sys.argv[3])
    except ValueError:
        sys.exit("Error: solo operandos numericos!")

    if sys.argv[2] == "suma":
        resultado = miCalculadora.suma(operando1, operando2)
    elif sys.argv[2] == "resta":
        resultado = miCalculadora.resta(operando1, operando2)
        pass
    else:
        sys.exit('Operacion solo puede ser sumar o restar.')

    print(resultado)
