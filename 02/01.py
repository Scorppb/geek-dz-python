# Напишите программу, которая принимает на вход вещественное число и показывает сумму его цифр.
# Пример:
# - 6782 -> 23
# - 0,56 -> 11

def sum_digits(x):                            
    if float(x) < 0:                          
        x = float(x) * (-1)
    number = 0
    for i in str(x):
        if i != '.':
            number += int(i)
    return number

x = input('Введите вещественное число> ')
print(f'Сумма чисел равна {sum_digits(x)}')
