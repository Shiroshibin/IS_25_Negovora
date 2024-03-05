"""
2. В квадратной матрице элементы на главной диагонали увеличить в 2 раза
"""
from random import randint

m_size = 3 

matrix = [[randint(0, 9) for _ in range(0, m_size)] for _ in range(0, m_size)]

print("start Matrix: ")
[print(i) for i in matrix]

[(matrix[i].insert(i, matrix[i][i] * 2), matrix[i].pop(i + 1))  for i in range(0, m_size)]
print("result Matrix: ")
[print(i) for i in matrix]
