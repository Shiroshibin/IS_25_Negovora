"""
Вариант 21. 

Дана строка «Петров Иван ПОКС-29 5 4 3 2 5 4 4 5 4». Преобразовать
информацию из строки в словарь, найти среднее арифметическое оценок,
результаты вывести на экран.

"""


# Заводим рабочие переменные

data_str_prime = "Петров Иван ПОКС-29 5 4 3 2 5 4 4 5 4"
data_str = data_str_prime.split("-")
data_dict = dict()



# Разделяем ключ и значение словаря

data_str[0] += f"-{data_str[-1].split(" ")[0]}"
data_str[-1] = data_str[-1].split(" ")[1:]
data_dict[data_str[0]] = list()



# Обрабатываем значение словаря в цифры

for i in data_str[-1]:
    data_dict[data_str[0]].append(int(i))



# Считаем среднее арифметическое значения словаря

data_average = sum(data_dict[data_str[0]]) / len(data_dict[data_str[0]])



print(f"Исходная строка: {data_str_prime}")
print(f"Словарь: {data_dict}")
print(f"Среднее арифметическое: {data_average}")