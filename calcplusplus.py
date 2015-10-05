#!/usr/bin/python3
# -*- coding: utf-8 -*-

import sys
import csv
import calcoohija

if __name__ == "__main__":

    calcu = calcoohija.CalculadoraHija()
    fichero = sys.argv[1]
    try:
        with open(fichero) as csvarchivo:
            lineas = csv.reader(csvarchivo)
            for linea in lineas:
                operador = linea[0]
                if operador == "suma":
                        sum1 = 0
                        for operaciones in linea[1:]:
                            sum1 = calcu.suma(sum1, float(operaciones))
                        print(sum1)
                if operador == "resta":
                    rest1 = calcu.resta(float(linea[1]), float(linea[2]))
                    for operaciones in linea[3:]:
                        rest1 = calcu.resta(rest1, float(operaciones))
                    print(rest1)
                if operador == "multiplica":
                    mult = 1
                    for operaciones in linea[1:]:
                        mult = calcu.multiplica(mult, float(operaciones))
                    print(mult)
                if operador == "divide":
                    if float(linea[2]) == 0:
                        sys.exit("Division by zero is not allowed")
                    else:
                        div = calcu.divide(float(linea[1]), float(linea[2]))
                    for operaciones in linea[3:]:
                        if float(operaciones) == 0:
                            sys.exit("Division by zero is not allowed")
                        else:
                            div = calcu.divide(div, float(operaciones))
                    print(div)
    except ValueError:
        sys.exit("Error: Non numerical parameters")
