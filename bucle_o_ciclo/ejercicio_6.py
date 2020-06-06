# -*- coding: utf-8 -*-

# imprimir los números impares desde el 100 al 1 e imprimir cuantos impares hay

i = 101
suma_impares = 0

while i >= 1:
    print(i)
    i = i - 2
    suma_impares = suma_impares + 1

print("El número de impares es: ")
print(suma_impares)
