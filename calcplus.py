#!/usr/bin/python3
# -*- coding: utf-8 -*-

import sys
import calcoohija
import calcoo


def operating(calc, operation, numbers):
    ans = int(numbers[0])
    for num in numbers[1:]:
        ans = calcoo.do_operation(calc, operation, ans, int(num))
    print(ans)


if __name__ == "__main__":
    script, filename = sys.argv
    calc = calcoohija.CalculadoraHija()
    file = open(filename)
    for line in file.readlines():
        operation = line.split(',')[0]
        numbers = line.split(',')[1:]
        operating(calc, operation, numbers)
    file.close
