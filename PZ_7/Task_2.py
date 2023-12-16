"""

2. Дана строка, состоящая из русских слов, разделенных пробелами (одним или
несколькими). Вывести строку, содержащую эти же слова, разделенные одним
символом «.» (точка). В конце строки точку не ставить

"""

Russian_String = "Строка состоящая из русских слов "

print(f"Russian_String = {Russian_String}")
print(f"Replace Russian_String = {Russian_String.replace(" ", ".") if Russian_String.replace(" ", ".")[-1] != "." else Russian_String.replace(" ", ".")[:-1]}")