# Вычислить число c заданной точностью d
# Пример:
# - при $d = 0.001, π = 3.141.$    $10^{-1} ≤ d ≤10^{-10}$

from math import pi
number = float(input('Введите число, для заданния точности числа Пи: '))
print('pi->', round(int(pi / number) * number, 10))