#!/usr/bin/python3
# -*- coding: utf-8 -*-

import sys
from calc import to_number
import calcoo
import calcoohija

def capture_argv_error():
    if len(sys.argv) != 2:
        sys.exit("Error: incorrect parameters\nUse: script filename ")


def operating(calc, operation, numbers):
    ans = int(numbers[0])
    for num in numbers[1:]:
        ans = calcoo.do_operation(calc, operation, ans, to_number(num))
    print(ans)


if __name__ == "__main__":
    capture_argv_error()
    filename = sys.argv[0]
    calc = calcoohija.CalculadoraHija()
    file = open(filename)
    for line in file.readlines():
        operation = line.split(',')[0]
        numbers = line.split(',')[1:]
        operating(calc, operation, numbers)
    file.close
