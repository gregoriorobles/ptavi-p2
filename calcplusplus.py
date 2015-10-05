#!/usr/bin/python3
# -*- coding: utf-8 -*-

import sys
import calcoo
import calcoohija
import calcplus
import csv


with open('prueba.csv', newline='') as File:

    reader = csv.reader(File)
    Calc = calcoohija.CalculadoraHija()

    for row in reader:
        Operation = row.pop(0)
        try:
            if Operation == 'suma':
                Result = 0
                for Op in row:
                    Result = Result + Calc.plus(int(Op), 0)
                print(Result)
            elif Operation == 'resta':
                # Saca el primer valor de la lista y lo elimina
                Result = int(row.pop(0))
                for Op in row:
                    # Suma todos los valores despues del primero
                    Sum = Calc.plus(int(Op), 0)
                    Result = Result - Sum
                print(Result)
            elif Operation == 'multiplica':
                Result = 1
                for Op in row:
                    Result = Result*Calc.product(int(Op), 1)
                print(Result)
            elif Operation == 'divide':
                Result = int(row.pop(0))
                try:
                    for Op in row:
                        # Divide el primer valor entre el siguiente y acumula
                        Result = Result/Calc.divide(int(Op), 1)
                    print(Result)
                except ZeroDivisionError:
                    sys.exit('Division by zero is not allowed')
            else:
                sys.exit('Possible operations: /suma/resta/divide/multiplica/')
        except ValueError:
            sys.exit("Non numerical parameters")
