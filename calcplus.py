#!/usr/bin/python3
# -*- coding: utf-8 -*-ç

import sys
import calcoo
import calcoohija

if __name__ == "__main__":
    fich = open("prueba.csv","r")
    lista = fich.readlines()
    num_lineas = len(lista)
    calc = calcoohija.CalculadoraHija()
    
    
    for linea in lista:
        componente = linea.split(",")
        operacion = componente[0]
        operandos = componente[1:]
        print (operacion)
        print (operandos)
       
        if operacion == "suma":
            resultado = calc.suma(int(operandos[0]), int(operandos[1]))
            for numero in operandos[2:]:
                resultado = calc.suma(int(resultado), int(numero))
            print(resultado)    
                
        elif operacion == "resta":
            resultado = calc.resta(int(operandos[0]), int(operandos[1]))
            for numero in operandos[2:]:
                resultado = calc.resta(int(resultado), int(numero))
            print(resultado)
            
        elif operacion == "multiplica":
            resultado = calc.producto(int(operandos[0]), int(operandos[1]))
            for numero in operandos[2:]:
                resultado = calc.producto(int(resultado), int(numero))
            print (resultado)
            
        elif operacion == "divide":
            resultado = calc.division(int(operandos[0]), int(operandos[1]))
            for numero in operandos[2:]:
                resultado = calc.division(int(resultado), int(numero))
            print (resultado)        
            
    fich.close()

