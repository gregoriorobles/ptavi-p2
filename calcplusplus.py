#!/usr/bin/python3
# -*- coding: utf-8 -*-

from sys import argv
import csv
import calcplus
import calcoohija


if __name__ == "__main__":
    script, filename = argv
    with open(filename) as file:
        calculator = calcoohija.CalculadoraHija()
        for line in csv.reader(file):
            operation = line[0]
            numbers = line[1:]
            calcplus.operating(calculator, operations, numbers)
