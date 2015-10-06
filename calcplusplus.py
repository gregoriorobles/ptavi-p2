#!/usr/bin/python3
# -*- coding: utf-8 -*-

import sys
import csv
import calcoohija

if __name__ == "__main__":

    calcu = calcoohija.CalculadoraHija()
    fichero = sys.argv[1]
    diccionario = {"suma": calcu.suma, "multiplica": calcu.multiplica, "resta": calcu.resta, "divide": calcu.divide} 

    with open(fichero) as csvarchivo:
        lineas = csv.reader(csvarchivo)
        for linea in lineas:
            operador = linea[0]
            if operador in ["suma", "multiplica", "resta","divide"]:
                calcular = linea[1]
                for operaciones in linea[2:]:
                    calcular = diccionario[operador](calcular, operaciones)
                print(calcular)
