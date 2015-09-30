#   ROBERTO YUBERO DE DIEGO
#!/usr/bin/python3
# -*- coding: utf-8 -*-


import sys

class Calculadora:

    def suma(self, op1, op2):
        """ Funcion suma"""
        return op1 + op2


    def resta(self, op1, op2):
        """ Funcion resta """
        return op1 - op2
    
    
class CalculadoraHija(Calculadora):

    def multiplicacion(self, operando1, operando2):
        return operando1 * operando2
        
    def division(self, operando1, operando2):
        if operando2 == 0:
            sys.exit("Division by zero is not allowed")
        else:
            return operando1 / operando2


if __name__ == "__main__":

    miCalculadora = CalculadoraHija()
    #comprobamos que los operandos de entrada sean numericos
    try:
        operando1 = int(sys.argv[1])
        operando2 = int(sys.argv[3])
    except ValueError:
        sys.exit("Error: solo operandos numericos!")
        
    #dependiendo de los argumentos realizamos una operacion u otra       
    if sys.argv[2] == "suma":
        resultado = miCalculadora.suma(operando1, operando2)
    elif sys.argv[2] == "resta":
        resultado = miCalculadora.resta(operando1, operando2)
    elif sys.argv[2] == "multiplica":
        resultado = miCalculadora.multiplicacion(operando1, operando2)
    elif sys.argv[2] == "divide":
        resultado = miCalculadora.division(operando1, operando2)    
    else:
        sys.exit('Solo operaciones de suma, resta, multiplicacion y division')

    print(resultado)        
        
        
  
