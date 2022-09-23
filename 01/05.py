# Напишите программу, которая принимает на вход координаты двух точек и находит расстояние 
# между ними в 2D пространстве.
# Пример:
# - A (3,6); B (2,1) -> 5,09
# - A (7,-5); B (1,-1) -> 7,21

def InputNumbers(inputText):
    check_input = False
    while not check_input:
        try:
            number = float(input(f'{inputText}'))
            check_input = True
        except ValueError:
            print('Введите корректные данные')
    return number

def Pifagor(x_A, y_A, x_B, y_B):
    from math import sqrt
    print('Расстояние между точками А и В: ',round(sqrt((x_A - x_B)**2 + (y_A - y_B)**2), 2))

print('Введите координаты точки А:')
x_A = InputNumbers('X: ')
y_A = InputNumbers('Y: ')
print("Введите координаты точки B:")
x_B = InputNumbers('X: ')
y_B = InputNumbers('Y: ')
Pifagor(x_A, y_A, x_B, y_B)

