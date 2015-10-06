#!/usr/bin/python3
# -*- coding: utf-8 -*-

from sys import argv
import csv
import calcplus
import calcoohija


if __name__ == "__main__":
    calcplus.capture_argv_error()
    script, filename = argv
    with open(filename) as file:
        calc = calcoohija.CalculadoraHija()
        for line in csv.reader(file):
            operation = line[0]
            numbers = line[1:]
            calcplus.operating(calc, operation, numbers)
