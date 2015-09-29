#!/usr/bin/python3
# -*- coding: utf-8 -*-

from sys import argv
import calcoohija
import calcoo


def operating(calculator, operation, numbers):
    ans = int(numbers[0])
    for num in numbers[1:]:
        ans = calcoo.do_operation(calculator, operation, ans, int(num))
    print(ans)


if __name__ == "__main__":
    script, filename = argv
    file = open(filename)
    calculator = calcoohija.CalculadoraHija()
    for line in file.readlines():
        operation = line.split(',')[0]
        numbers = line.split(',')[1:]
        operating(calculator, operation, numbers)
    file.close
