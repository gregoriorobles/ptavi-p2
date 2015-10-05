#!/usr/bin/python3
# -*- coding: utf-8 -*-

import sys
import calcoohija

if __name__ == "__main__":

    leer = open(sys.argv[1], "r")
    lineas = leer.readlines()
    calcu = calcoohija.CalculadoraHija()

    for linea in (lineas):
        palabra = linea.split(",")
        operador = palabra[0]
        if operador == "suma":
            sum1 = 0
            for operaciones in palabra[1:]:
                sum1 = calcu.suma(sum1, operaciones)
            print(sum1)
        if operador == "resta":
            rest1 = calcu.resta(palabra[1], palabra[2])
            for operaciones in palabra[3:]:
                rest1 = calcu.resta(rest1, operaciones)
            print(rest1)
        if operador == "multiplica":
            mult = 1
            for operaciones in palabra[1:]:
                mult = calcu.multiplica(mult, operaciones)
            print(mult)
        if operador == "divide":
            if palabra[2] == 0:
                sys.exit("Division by zero is not allowed")
            else:
                div = calcu.divide(palabra[1], palabra[2])
            for operaciones in palabra[3:]:
                if operaciones == 0:
                    sys.exit("Division by zero is not allowed")
                else:
                    div = calcu.divide(div, operaciones)
            print(div)

