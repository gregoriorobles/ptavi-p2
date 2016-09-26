#!/usr/bin/python3
# -*- coding: utf-8 -*-

"""
Script de comprobación de entrega de práctica

Para ejecutarlo, desde la shell:
 $ python check-p2.py login_github

"""

import os
import random
import sys


if len(sys.argv) != 2:
    print()
    sys.exit("Usage : $ python3 check-p2.py login_github")

repo_git = "http://github.com/" + sys.argv[1] + "/ptavi-p2"

python_files = [
    'calc.py',
    'calcoo.py',
    'calcoohija.py',
    'calcplus.py',
    'calcplusplus.py',
    'esqueleto-oo.py'
    ]

files = ['README.md',
         'LICENSE',
         '.gitignore',
         'check-p2.py',
         '.git'
         ]

aleatorio = str(int(random.random() * 1000000))

error = 0

print()
print("Clonando el repositorio " + repo_git + "\n")
os.system('git clone ' + repo_git + ' /tmp/' + aleatorio + ' > /dev/null 2>&1')
try:
    student_file_list = os.listdir('/tmp/' + aleatorio)
except OSError:
    error = 1
    print("Error: No se ha podido acceder al repositorio " + repo_git + ".")
    print()
    sys.exit()

if len(student_file_list) != len(files) + len(python_files):
    error = 1
    print("Error: solamente hay que subir al repositorio los ficheros")
    print("indicados en las guion de practicas, que son en total")
    print(str(len(python_files) + len(files)) + " (incluyendo .git):")

for filename in files + python_files:
    if filename not in student_file_list:
        error = 1
        print("  Error: " + filename + " no encontrado.",
              "Tienes que subirlo al repositorio.")

if not error:
    print("Parece que la entrega se ha realizado bien.")
    print()
    print("La salida de pep8 es: (si todo va bien, no ha de mostrar nada)")
    print()
    files = ''
    for python_file in python_files:
        files += ' /tmp/' + aleatorio + '/' + python_file
    os.system('pep8 --repeat --show-source --statistics ' + files)
print()
