#!/usr/bin/python3
# -*- coding: utf-8 -*-

import sys
import calcoohija

if __name__ == "__main__":
    leer = open(sys.argv[1],"r")
    lineas = leer.readlines()

    for linea in lineas:
        #print(linea[:-1])
        palabra = linea.split(",")[:-1]
        #print (palabra) 
        operador=palabra[0]
        calc= calcoohija.CalculadoraHija()
        print(operador)
        if operador == "suma":
            while op <= palabra[-1] :
                op=palabra[1]
                op1=palabra[2]
                 sum1=op+op1
                for sum1 in palabra[:-1]
                resultado=calc.suma(op,op1)
        if operador == "resta":
           resultado=calcu.resta(palabra[2:-1])
        else:
            sys.exit("MAL")
           
        print(resultado)
     
        
