#!/usr/bin/python3
# -*- coding: utf-8 -*-

import sys
import csv
import calcoohija

if __name__ == "__main__":

    calcu = calcoohija.CalculadoraHija()
    fichero = sys.argv[1]
    with open(fichero) as csvarchivo:
        lineas = csv.reader(csvarchivo)
        for linea in lineas:
            operador = linea[0]
            if operador == "suma":
                    sum1 = 0
                    for operaciones in linea[1:]:
                        sum1 = calcu.suma(sum1, operaciones)
                    print(sum1)
            if operador == "resta":
                rest1 = calcu.resta(linea[1], linea[2])
                for operaciones in linea[3:]:
                    rest1 = calcu.resta(rest1, operaciones)
                print(rest1)
            if operador == "multiplica":
                mult = 1
                for operaciones in linea[1:]:
                    mult = calcu.multiplica(mult, operaciones)
                print(mult)
            if operador == "divide":
                div = calcu.divide(linea[1], linea[2])
                for operaciones in linea[3:]:
                    div = calcu.divide(div, operaciones)
                print(div)
