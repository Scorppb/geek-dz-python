# Напишите программу, которая найдёт произведение пар чисел списка. Парой считаем первый и 
# последний элемент, второй и предпоследний и т.д.
# Пример:
# - [2, 3, 4, 5, 6] => [12, 15, 16];
# - [2, 3, 5, 6] => [12, 15]

import random
number = int(input('Введите число> '))
number_list = []
for i in range(number):
   number_list.append(random.randint(1,10))
print(number_list)
new_list = []
for i in range((len(number_list)+1)//2):
    new_list.append(number_list[i]*number_list[len(number_list)-1-i])
print(new_list)


