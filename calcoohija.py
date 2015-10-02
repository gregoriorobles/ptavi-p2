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


class CalculadoraHija(Calculadora):

    def multiplicacion(self, operando1, operando2):
        return operando1 * operando2

    def division(self, operando1, operando2):
        if operando2 == 0:
            sys.exit("Division by zero is not allowed")
        else:
            return operando1 / operando2

    def operar(self, operacion, op1, op2):

        if operacion == "suma":
            return self.suma(op1, op2)
        elif operacion == "resta":
            return self.resta(op1, op2)
        elif operacion == "multiplica":
            return self.multiplicacion(op1, op2)
        elif operacion == "divide":
            return self.division(op1, op2)
        else:
            sys.exit('Operaciones admitidas: suma,' +
                     + 'resta, multiplicacion y division')


if __name__ == "__main__":

    miCalculadora = CalculadoraHija()
    #comprobamos que los operandos de entrada sean numericos
    try:
        operando1 = int(sys.argv[1])
        operando2 = int(sys.argv[3])
    except ValueError:
        sys.exit("Error: solo operandos numericos enteros")

    #realizamos la operacion
    resultado = miCalculadora.operar(sys.argv[2], operando1, operando2)
    print(resultado)
