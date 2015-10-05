#!/usr/bin/python3
# -*- coding: utf-8 -*-


import sys
import calcoo
import calcoohija
import csv


if __name__ == "__main__":
    calchija = calcoohija.CalculadoraHija()
    with open(sys.argv[1]) as fichero:
        reader = csv.reader(fichero)
        for ListaNumeros in reader:

            Operacion = ListaNumeros.pop(0)

            if Operacion == 'suma':
                suma = calchija.plus(int(ListaNumeros[0]), int(ListaNumeros[1]))
                for numero in ListaNumeros[2:]:
                    suma = calchija.plus(suma, int(numero))
                print(suma)

            elif Operacion == 'resta':
                resta = calchija.minus(int(ListaNumeros[0]), int(ListaNumeros[1]))
                for numero in ListaNumeros[2:]:
                    resta = calchija.minus(resta, int(numero))
                print(resta)

            elif Operacion == 'multiplica':
                multi = calchija.multi(int(ListaNumeros[0]), int(ListaNumeros[1]))
                for numero in ListaNumeros[2:]:
                    multi = calchija.multi(multi, int(numero))
                print(multi)

            elif Operacion == 'divide':
                div = calchija.div(int(ListaNumeros[0]), int(ListaNumeros[1]))
                for numero in ListaNumeros[2:]:
                    div = calchija.div(div, int(numero))
                    print(div)
