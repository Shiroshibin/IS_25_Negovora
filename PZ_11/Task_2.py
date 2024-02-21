"""

Вариант 21.

2. Из предложенного текстового файла (text18-21.txt) вывести на экран его содержимое,
количество знаков препинания. Сформировать новый файл, в который поместить текст в
стихотворной форме выведя строки в обратном порядке.

"""
from string import punctuation


with open("PZ_11//text18-21.txt", "r", encoding = "UTF-8") as file:
    text = file.read()

with open("PZ_11//result.txt", "w", encoding = "UTF-8") as file:
    file.writelines([i + "\n" for i in text.splitlines()[::-1]])

print(text)
print(f"\nКоличество знаков препинания: {len([i for i in list(text) if i in punctuation])}")