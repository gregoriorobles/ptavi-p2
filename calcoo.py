#!/usr/bin/python3
# -*- coding:utf-8 -*-

import sys


class Calculadora():
    def sum(self, a, b):
        return a + b

    def substraction(self, a, b):
        return a - b


def to_number(num):
    try:
        if '.' in num:
            return float(num)
        else:
            return int(num)
    except:
        sys.exit("Error")


def do_operation(operation, op1, op2):
    calculator = Calculadora()


    if operation == "suma":
        result = calculator.sum(op1, op2)
        print(result)

    elif operation == "resta":
        result = calculator.substraction(op1, op2)
        print(result)

    else:
        print ("Not allowed operation", operation)

if __name__ == "__main__":
    op1 = to_number(sys.argv[1])
    operation = sys.argv[2]
    op2 = to_number(sys.argv[3])
    do_operation(operation, op1, op2)
