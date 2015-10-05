#!/usr/bin/python3
# -*- coding: utf-8 -*-

import sys
import calcoohija

if __name__ == "__main__":

    leer = open(sys.argv[1], "r")
    lineas = leer.readlines()
    calcu = calcoohija.CalculadoraHija()
    try:
        for linea in (lineas):
            palabra = linea.split(",")
            operador = palabra[0]
            if operador == "suma":
                sum1 = 0
                for operaciones in palabra[1:]:
                    sum1 = calcu.suma(sum1, float(operaciones))
                print(sum1)
            if operador == "resta":
                rest1 = calcu.resta(float(palabra[1]), float(palabra[2]))
                for operaciones in palabra[3:]:
                    rest1 = calcu.resta(rest1, float(operaciones))
                print(rest1)
            if operador == "multiplica":
                mult = 1
                for operaciones in palabra[1:]:
                    mult = calcu.multiplica(mult, float(operaciones))
                print(mult)
            if operador == "divide":
                if float(palabra[2]) == 0:
                    sys.exit("Division by zero is not allowed")
                else:
                    div = calcu.divide(float(palabra[1]), float(palabra[2]))
                for operaciones in palabra[3:]:
                    if float(operaciones) == 0:
                        sys.exit("Division by zero is not allowed")
                    else:
                        div = calcu.divide(div, float(operaciones))
                print(div)
    except ValueError:
        sys.exit("Error: Non numerical parameters")
