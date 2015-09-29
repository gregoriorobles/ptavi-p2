#!/usr/bin/python3
# -*- coding: utf-8 -*-

import sys


def to_number(num):
    try:
        if '.' in num:
            return float(num)
        else:
            return int(num)
    except:
        sys.exit("Error: Non numerical parameters")


def sum(op1, op2):
    return op1 + op2


def substraction(op1, op2):
    return op1 - op2


def do_operation(operations, operation, op1, op2):

    try:
        return operations[operation](op1, op2)
    except KeyError:
        sys.exit("Not allowed operation " + operation)


if __name__ == "__main__":
    operations = {"suma": sum, "resta": substraction}
    op1 = to_number(sys.argv[1])
    operation = sys.argv[2]
    op2 = to_number(sys.argv[3])
    print(do_operation(operations, operation, op1, op2))
