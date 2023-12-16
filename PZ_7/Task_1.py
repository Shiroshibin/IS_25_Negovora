from random import randint

"""

Вариант 21

1. Дано целое положительное число. Вывести символы, изображающие цифры этого
числа (в порядке справа налево).


"""

Random_Integer = randint(10, 9999)
print(f"Random_Integer = {Random_Integer}")
print(f"Revers Random_Integer = {str(Random_Integer)[::-1]}")