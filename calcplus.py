#   ROBERTO YUBERO DE DIEGO
#!/usr/bin/python3
# -*- coding: utf-8 -*-


import sys
import calcoohija



if __name__ == "__main__":

    fichero = open(sys.argv[1], 'r')
    lista_lineas = fichero.read()     #leo todo el fichero   
    lista_lineas = lista_lineas.splitlines() #creamos una lista de lineas sin salto de linea
    miCalculadora = calcoohija.CalculadoraHija()
    
    
    for i in range(0,len(lista_lineas)):                      #recorro la lista linea por linea   
        lista_lineas[i] = lista_lineas[i].split(',')    #eliminamos las comas de cada linea
        linea = lista_lineas[i]                         #separo cada linea y la guardo en una variable                       
        operacion = linea[0]                            #elijo el tipo de operacion de la linea      
        resultado = int(linea[1])                       #el primer operando lo meto directamente en resultado
        
        for k in range(2,len(linea)):                   #recorro la linea desde 2operando
            operando = int(linea[k])
            resultado = miCalculadora.operar(operacion, resultado, operando)
            
        print(operacion + " = " + str(resultado))
            

    
    

    fichero.close()
