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
        resultado = int(linea[1])                       #el primer operando lo meto directamente en resultado 
              
        for k in range(2,len(linea)):                   #recorro la linea desde 2operando
            operando = int(linea[k])
            resultado = miCalculadora.operar(operacion, resultado, operando)
            
        print(operacion + " = " + str(resultado))
      
