# Напишите программу, которая принимает на вход координаты точки (X и Y), причём X ≠ 0 и Y ≠ 0 
# и выдаёт номер четверти плоскости, в которой находится эта точка (или на какой оси она находится).
# Пример:
# - x=34; y=-30 -> 4
# - x=2; y=4-> 1
# - x=-34; y=-30 -> 3

def InputNumbers(inputText):
    check_input = False
    while not check_input:
        try:
            number = int(input(f'{inputText}'))
            check_input = True
        except ValueError:
            print('Введите корректные данные')
    return number

def CheckQuarterCoordinates(x, y):
    if x == 0 or y == 0:
        print('Введите число, не равное 0')
    elif x > 0 and y > 0:
        print('Номер четверти = 1')
    elif x < 0 and y > 0:
        print('Номер четверти = 2')
    elif x < 0 and y < 0:
        print('Номер четверти = 3')
    elif x > 0 and y < 0:
        print('Номер четверти = 4')

x = InputNumbers('Введите координату точки x: ')
y = InputNumbers('Введите координату точки y: ')
CheckQuarterCoordinates(x, y)