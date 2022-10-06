# Задайте список из нескольких чисел. Напишите программу, которая найдёт сумму элементов списка, 
# стоящих на нечётной позиции.
# Пример:
# - [2, 3, 5, 9, 3] -> на нечётных позициях элементы 3 и 9, ответ: 12

import random
number = int(input('Введите число> '))
number_list = []
for i in range(number):
   number_list.append(random.randint(1,10))
print(number_list)
print(sum(number_list[1::2]))

