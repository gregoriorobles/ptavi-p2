#!/usr/bin/python3
# -*- coding: utf-8 -*-

import sys
import calcoohija

if __name__ == "__main__":
    leer = open(sys.argv[1],"r")
    lineas = leer.readlines()
    calcu= calcoohija.CalculadoraHija()
    for linea in (lineas):
        #print(linea[:-1])
        palabra = linea.split(",")
        #print (palabra) 
        operador=palabra[0]
       
        print(operador)
       
        if operador == "suma":
            sum1=0
            for operaciones in palabra[1:]:
                sum1=calcu.suma (sum1, int(operaciones))
            print(sum1)
            
            
        #if operador == "resta":
         #  resultado=calcu.resta(palabra[2:-1])
        #else:
         #   sys.exit("MAL")
           
        #print(resultado)
     
