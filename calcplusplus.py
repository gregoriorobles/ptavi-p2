#!/usr/bin/python3
# -*- coding: utf-8 -*-

import sys
import calcplus
import csv
fichero= sys.argv[1]
with open(fichero) as csvarchivo:
    lineas = csv.reader(csvarchivo)
    for linea in lineas:
        print(linea)
       
        operacion, op1, op2 = linea
        print(operacion, op1, op2, op3)
