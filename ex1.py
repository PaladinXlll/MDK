# Найти площадь и периметр прямоугольного треугольника
import math

AB = float(input('Длина первого катета:\n'))
AC = float(input('Длина второго катета:\n'))

BC = math.sqrt(AB ** 2 + AC ** 2)

S = (AB * AC) / 2
P = AB + AC + BC

print('Площадь треугольника =', S, '\nПериметр треугольника =', P)
