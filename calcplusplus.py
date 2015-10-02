#   ROBERTO YUBERO DE DIEGO
#!/usr/bin/python3
# -*- coding: utf-8 -*-


import calcoohija
import csv
import sys

with open(sys.argv[1], 'rd') as f:
    lista_lineas = csv.reader(f)
    miCalculadora = calcoohija.CalculadoraHija()

    for linea in lista_lineas:
        operacion = linea[0]
        #el primer operando lo meto directamente en resultado
        resultado = int(linea[1])

        #recorro la linea desde 2operando
        for k in range(2, len(linea)):
            operando = int(linea[k])
            resultado = miCalculadora.operar(operacion, resultado, operando)

        print(operacion + " = " + str(resultado))
