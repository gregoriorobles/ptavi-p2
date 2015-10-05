#!/usr/bin/python3
# -*- coding: utf-8 -*-

import sys

from calcoo import Calculadora

class CalculadoraHija(Calculadora):

	def mult(self, op1, op2):
		""" Function to multiply the operands """
		return op1 * op2


	def divide(self, op1, op2):
		""" Function to divide the operands """
		return op1 / op2
