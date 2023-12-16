from random import randint

"""

3. Дано множество A из N точек на плоскости и точка B (точки заданы своими
координатами х, у). Найти точку из множества A, наиболее близкую к точке B.
Расстояние R между точками с координатами (x1, y1) и (x2, у2) вычисляется по
формуле:
R = √((x^2 – x^1)^2 + (у^2 – y^1)^2)

"""


#  0 0 0 0 0 0 0 0 0 0 0
#  0 0 0 0 0 0 0 0 0 0 1
#  0 0 0 0 0 0 0 0 0 0 0
#  0 0 0 0 0 0 0 0 0 0 0
#  0 0 0 0 0 0 0 0 0 2 0
#  0 0 0 0 0 1 0 0 0 0 0
#  0 0 0 0 0 0 0 0 0 0 0
#  0 0 0 0 0 0 0 0 0 0 0
#  0 0 0 0 0 0 0 0 0 0 0
#  0 0 0 0 0 0 0 0 0 0 0
#  0 0 0 0 0 0 0 0 0 0 0




A = set()
B = (randint(1, 5), randint(1, 5))
N = randint(1, 5)

print(f"N = {N}")

# Заполняем множество N количеством уникальных точек и переводим его в список для удобной работы
while len(A) != N:
    A.add((randint(1, 5), randint(1, 5)))
A = list(A)


print(f"A = {A}")
print(f"B = {B}")

# Считаем все R и записываем их в список
R_list = list()
for i in A:
    R = ( ( ( i[0] - B[0] ) ** 2 ) + ( ( i[1] - B[1] ) ** 2 ) ) ** 0.5
    R_list.append(R)

# Берем минимальный R, получаем его индекс и по этому индексу находим нужную точку в списке A
print(A[R_list.index(min(R_list))])