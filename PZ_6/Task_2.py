from random import randint

"""
Вариант 21

2. Дан целочисленный список размера N. Если он является перестановкой, то есть
содержит все числа от 1 до N, то вывести 0; в противном случае вывести номер
первого недопустимого элемента.

"""

# Генерим данные
N = randint(5, 10)

print(f"N = {N}")

# Создаем список и заполняем его
data_list = list()
for i in range(0, N):
    data_list.append(randint(0, 10))

# # Создаем список и заполняем его для вывода 0
# data_list = list()
# for i in range(1, N + 1):
#     data_list.append(i)

print(f"data_list = {data_list}")

# # Генератор для проверки диапозона
# print(*(i for i in range(1, N + 1)))

# Если все числа в списке уникальны и входят в нужный диапозон, то выводим 0
# Если все числа уникальны, но 1 не входит в промежуток, то выводим номер этого числа
# Если в списке есть дубли, выводим первое повторяющиеся число
if len(set(data_list)) == N:

    range_N = range(1, N + 1)
    response = "0"
    for i in data_list:
        if i not in range_N:
            response = f"{data_list.index(i) + 2} число не в нужном диапозоне"
            break

    print(response)

else:
    for i in data_list:
        if data_list.count(i) != 1:
            print(f"{data_list.index(i) + 2} число - дублируется в списке")
            break