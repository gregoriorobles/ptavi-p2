#!/usr/bin/python3
# -*- coding: utf-8 -*-ç

import sys
import calcoo
import calcoohija
import csv

if __name__ == "__main__":
    
    calc = calcoohija.CalculadoraHija()
    with open(sys.argv[1]) as fichero:
        reader = csv.reader(fichero)
        for operandos in reader:
           
            print (operandos)
            operacion = operandos[0]
           
            if operacion == "suma":
                resultado = calc.suma(int(operandos[1]), int(operandos[2]))
                for numero in operandos[3:]:
                    resultado = calc.suma(int(resultado), int(numero))
                print(resultado)    
                    
            elif operacion == "resta":
                resultado = calc.resta(int(operandos[1]), int(operandos[2]))
                for numero in operandos[3:]:
                    resultado = calc.resta(int(resultado), int(numero))
                print(resultado)
                
            elif operacion == "multiplica":
                resultado = calc.producto(int(operandos[1]), int(operandos[2]))
                for numero in operandos[3:]:
                    resultado = calc.producto(int(resultado), int(numero))
                print (resultado)
                
            elif operacion == "divide":
                resultado = calc.division(int(operandos[1]), int(operandos[2]))
                for numero in operandos[3:]:
                    resultado = calc.division(int(resultado), int(numero))
                print (resultado)        
                
           

