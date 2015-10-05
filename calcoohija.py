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
    calc.capture_argv_error()
    op1, operation, op2 = calc.take_args()
    calc = CalculadoraHija()
    print(calcoo.do_operation(calc, operation, op1, op2))
