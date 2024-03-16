"""
В исходном текстовом файле (hotline.txt) после фразы «Горячая линия» добавить
фразу «Министерства образования Ростовской области», посчитать количество
произведённых добавлений. Сколько номеров телефонов заканчивается на «03»,
«50». Вывести номера телефонов горячих линий, связанных с ЕГЭ/ГИА.
"""

import re

with open("PZ_14\hotline.txt", "r", encoding="UTF-8") as file:
    text = file.read()

count = len(re.findall(r"«Горячая линия»", text))

text = re.sub(r"«Горячая линия»", 
       "«Горячая линия Министерства образования Ростовской области»",
       text)

with open("PZ_14\hotline_result.txt", "w+", encoding="UTF-8") as file:
    file.write(text)

print(f"Количество произведённых добавлений: {count}")



num_03 = len(re.findall(r"((8|\+7|7)(\d{8})(03))|((8|\+7|7)(\d{8}-)(03))|((8|\+7|7)(\d{7})(03))", text))
num_50 = len(re.findall(r"((8|\+7|7)(\d{8})(50))|((8|\+7|7)(\d{8}-)(50))|((8|\+7|7)(\d{7})(50))", text))

print(f"Число номеров, заканчивающихся на 03: {num_03}")
print(f"Число номеров, заканчивающихся на 50: {num_50}")



ecs_num = re.findall(r"(ЕГЭ|ГИА)(.*)?", text)

num = re.compile(r"((8|\+7|7)(\d{10}))|((8|\+7|7)(\d{8}-\d{2}))|((8|\+7|7)(\d{9}))")

res = list()
for i in ecs_num:
    res.append(num.search(i[1]).group(0))
    
res = ", ".join(res)
print(f"Номера горячих линий, связанных с ЕГЭ/ГИА: {res}")