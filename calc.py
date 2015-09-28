#!/usr/bin/python3
# -*- coding: utf-8 -*-

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
        sys.exit("Error")


def sum(op1, op2):
    return op1 + op2


def substraction(op1, op2):
    return op1 - op2


def do_operation(operation, op1, op2):
    if operation == "suma":
        print(sum(op1, op2))
    elif operation == "resta":
        print(substraction(op1, op2))
    else:
        print ("Not allowed operation ", operation)

if __name__ == "__main__":
    op1 = to_number(sys.argv[1])
    operation = sys.argv[2]
    op2 = to_number(sys.argv[3])
    do_operation(operation, op1, op2)
