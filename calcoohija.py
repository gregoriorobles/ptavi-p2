#!/usr/bin/python3
# -*- coding:utf-8 -*-

import sys
import calc
import calcoo


class CalculadoraHija(calcoo.Calculadora):

    def __init__(self):
        super().__init__()
        self.operations["multiplica"] = self.multiply
        self.operations["divide"] = self.division

    def multiply(self, a, b):
        return a * b

    def division(self, a, b):
        try:
            return a / b
        except ZeroDivisionError:
            sys.exit("Division by zero is not allowed")


if __name__ == "__main__":
    op1 = calc.to_number(sys.argv[1])
    operation = sys.argv[2]
    op2 = calc.to_number(sys.argv[3])
    calculator = CalculadoraHija()
    print(calcoo.do_operation(calculator, operation, op1, op2))
