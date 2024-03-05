"""
Вариант 21.
1. В матрице найти минимальный элемент в предпоследней строке.
"""
from random import randint

matrix = [[randint(10, 99) for _ in range(0, 10)] for _ in range(0, 10)]

print("Matrix: ")
[print(i) for i in matrix]
print(f"min_value: {min(matrix[len(matrix) - 2])}")
