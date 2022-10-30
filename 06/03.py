# Дана последовательность чисел. Получить список уникальных элементов заданной последовательности.
# *Пример:*
# [1, 2, 3, 5, 1, 5, 3, 10] => [2, 10]

enum_number = list(map(int, input("input list:").split()))
enum_unique = list(filter(lambda item: enum_number.count(item) == 1, enum_number))
print(enum_number, '->', enum_unique)
