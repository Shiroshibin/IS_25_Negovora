"""
2.Из заданной строки отобразить только цифры. Использовать библиотекуstring.
Строка - TheGreatPyramidofKhufuatGizawasbuiltabout 2700 BC, 755 feet (230metres) longand
481 feet (147 metres) high.
"""

data = "TheGreatPyramidofKhufuatGizawasbuiltabout 2700 BC, 755 feet (230metres) longand 481 feet (147 metres) high."

def get_all_digit(data: str):
    yield [i for i in data if i.isdigit()]

data = get_all_digit(data)
print(*data)