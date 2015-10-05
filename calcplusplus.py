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
            diccionario = {"suma": calcu.suma, "multiplica": calcu.multiplica, "resta": calcu.resta, "divide": calcu.divide} 

        if operador in ["suma", "multiplica", "resta","divide"]:
            calcular = palabra[1]
            for operaciones in palabra[2:]:
                calcular = diccionario[operador](calcular, operaciones)
            print(calcular)
