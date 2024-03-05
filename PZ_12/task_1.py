"""
Вариант 21.
1.Даны две последовательности. Найти элементы, различные для двух
последовательностей и их среднее арифметическое.
"""

import random 

list_one = [random.randint(1, 5) for _ in range(0, 3)]
list_two = [random.randint(1, 5) for _ in range(0, 2)]

unique_el = [i for i in list_one if i not in list_two]
unique_el.extend([i for i in list_two if i not in list_one])

while len(list_one) > len(list_two):
    list_two.append(0)
while len(list_two) > len(list_one):
    list_one.append(0)

midle: list = [x + y for x, y in zip(list_one, list_two)]
print(f"midle: {midle}")
midle = sum(midle) / (len(midle) * 2)



print(f"list_one: {list_one}")
print(f"list_two: {list_two}")
print(f"unique_el: {list(set(unique_el))}")
print(f"midle: {round(midle, 3)}")