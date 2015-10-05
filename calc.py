#!/usr/bin/python3
# -*- coding: utf-8 -*-

import sys


def to_number(num):
    try:
        if '.' in num:
            return float(num)
        else:
            return int(num)
    except ValueError:
        sys.exit("Error: Non numerical parameters")


def take_args():
    if len(sys.argv) != 4:
        sys.exit("Error: incorrect parameters\nUse: script op1 operation op2")
    else:
        op1 = to_number(sys.argv[1])
        operation = sys.argv[2]
        op2 = to_number(sys.argv[3])
        return op1, operation, op2


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
    op1, operation, op2 = take_args()
    operations = {"suma": sum, "resta": substraction}
    print(do_operation(operations, operation, op1, op2))
