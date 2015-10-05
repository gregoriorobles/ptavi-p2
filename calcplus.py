#!/usr/bin/python3
# -*- coding: utf-8 -*-

import sys
import calcoo
import calcoohija


if __name__ == '__main__':

    Calc = calcoohija.CalculadoraHija()
    File = open('prueba.csv', 'r')
    List = File.readlines()
    for LineNum in List:
        # LineNum es directamente el elemento de la lista, no la posicion.
        NumberList = LineNum.split(',')
        # Crea una lista con los elementos que van separados por comas.
        Operation = NumberList.pop(0)
        try:
            if Operation == 'suma':
                Result = 0
                for Op in NumberList:
                    Result = Result + Calc.plus(int(Op), 0)
                print(Result)
            elif Operation == 'resta':
                Result = int(NumberList.pop(0))
                Sum = 0
                for Op in NumberList:
                    # A-B-C-D = A - (B + C + D)
                    Sum = Sum + Calc.plus(int(Op), 0)
                Result = Result - Sum
                print(Result)
            elif Operation == 'multiplica':
                Result = 1
                for Op in NumberList:
                    Result = Result*Calc.product(int(Op), 1)
                print(Result)
            elif Operation == 'divide':
                Result = int(NumberList.pop(0))
                try:
                    for Op in NumberList:
                        Result = Result/Calc.divide(int(Op), 1)
                    print(Result)
                except ZeroDivisionError:
                    sys.exit('Division by zero is not allowed')
            else:
                sys.exit('Possible operations: /suma/resta/divide/multiplica/')
        except ValueError:
            sys.exit("Non numerical parameters")

    File.close()
