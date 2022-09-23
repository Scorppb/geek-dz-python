# Напишите программу, которая по заданному номеру четверти, показывает диапазон возможных 
# координат точек в этой четверти (x и y).

def InputNumbers(inputText):
    check_input = False
    while not check_input:
        try:
            number = int(input(f'{inputText}'))
            check_input = True
        except ValueError:
            print('Введите корректные данные')
    return number

def CheckNumber(number):
    if number < 1 or number > 4:
        print('Введите число, соответствующее четверти системы координат')
    elif number == 1:
        print('x > 0, y > 0')
    elif number == 2:
        print('x < 0, y > 0')
    elif number == 3:
        print('x < 0, y < 0')
    elif number == 4:
        print('x > 0, y < 0')

number = InputNumbers('Введите номер четверти системы координат: ')
CheckNumber(number)