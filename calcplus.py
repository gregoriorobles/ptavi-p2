#   ROBERTO YUBERO DE DIEGO
#!/usr/bin/python3
# -*- coding: utf-8 -*-


import sys
import calcoohija


if __name__ == "__main__":

    fichero = open(sys.argv[1], 'r')
    #leo todo el fichero
    lista_lineas = fichero.read()
    #creamos una lista de lineas sin salto de linea
    lista_lineas = lista_lineas.splitlines()
    miCalculadora = calcoohija.CalculadoraHija()

    #recorro la lista linea por linea
    for i in range(0, len(lista_lineas)):
        #eliminamos las comas de cada linea
        lista_lineas[i] = lista_lineas[i].split(',')
        #separo cada linea y la guardo en una variable
        linea = lista_lineas[i]
        #elijo el tipo de operacion de la linea
        operacion = linea[0]
        #el primer operando lo meto directamente en resultado

        #recorro la linea desde 2operando
        for k in range(2, len(linea)):
            operando = int(linea[k])
            resultado = miCalculadora.operar(operacion, resultado, operando)

        print(operacion + " = " + str(resultado))

    fichero.close()
