"""

Вариант 21.

1. Средствами языка Python сформировать два текстовых файла (.txt), содержащих по одной
последовательности из целых положительных и отрицательных чисел. Сформировать
новый текстовый файл (.txt) следующего вида, предварительно выполнив требуемую
обработку элементов:

Содержимое первого файла:
Отрицательные элементы:
Количество отрицательных элементов:
Среднее арифметическое:
Содержимое второго файла:
Положительные элементы:
Количество положительных элементов:
Сумма положительных элементов:

"""

from random import randint



first_list = [randint(-10, 10) for i in range(0, 10)]
second_list = [randint(-10, 10) for i in range(0, 10)]



with open("first.txt", "w+", encoding="UTF-8") as file:
    file.write(str(first_list)[1:-1])
with open("second.txt", "w+", encoding="UTF-8") as file:
    file.write(str(second_list)[1:-1])



with open("first.txt", "r") as file:
    first_file = [int(i) for i in file.read().split(",")]
with open("second.txt", "r") as file:
    second_file = [int(i) for i in file.read().split(",")]


negative_list = [i for i in first_file + second_file if i < 0]
pozitiv_list = [i for i in first_file + second_file if i > 0]
midle_list = sum(first_file + second_file) / len(first_file + second_file)

result_text = f"Содержимое первого файла: {str(first_file)[1:-1]}\n\
Отрицательные элементы: {str(negative_list)[1:-1]}\n\
Количество отрицательных элементов: {len(negative_list)}\n\
Среднее арифметическое: {midle_list}\n\
Содержимое второго файла: {str(second_file)[1:-1]}\n\
Положительные элементы: {str(pozitiv_list)[1:-1]}\n\
Количество положительных элементов: {len(pozitiv_list)}\n\
Сумма положительных элементов: {sum(pozitiv_list)}"

with open("result.txt", "w", encoding="UTF-8") as file:
    file.write(result_text)