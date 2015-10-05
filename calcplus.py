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
        diccionario = {"suma": calcu.suma, "multiplica": calcu.multiplica, "resta": calcu.resta, "divide": calcu.divide}

        if operador in ["suma", "multiplica", "resta", "divide"]:
            calcular = palabra[1]
            for operaciones in palabra[2:]:
                calcular = diccionario[operador](calcular, operaciones)
            print(calcular)
