# Задайте последовательность чисел. Напишите программу, которая выведет список неповторяющихся 
# элементов исходной последовательности.

enum_number = [1, 2, 2, 3, 4, 4, 5, 6, 6, 6, 7]
enum_unique = list(filter(lambda item: enum_number.count(item) == 1, enum_number))
print(enum_number, '->', enum_unique)
