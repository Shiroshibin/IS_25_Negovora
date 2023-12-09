def main():
    """
    Negovora Nikita IS-25 Вариант 21

    1.  
        Дано трехзначное число. 
        Проверить истиность высказывания "Все цифры данного числа различны"
    2.
        Даны два числа.
        Вывести порядковый номер меньшего из них.
    """

    # Вызов функции для первого задания
    # task_1()

    # Вызов функции для второго задания
    task_2()

    

# Функция для первого задания
def task_1():
    """
        Дано трехзначное число. 
        Проверить истиность высказывания "Все цифры данного числа различны".
    """

    # Запрашиваем у пользователя число 
    # ("input_number: str = ..." означает, что переменная input_number ожидается строкой)
    input_number: str = input("Введите трехзначное число: ")

    # Проверка на то, является ли введеное значение целым числом
    try:
        int(input_number)
    except:
        print("ОШИБКА! Вы ввели не целое число.")
        return False

    # Проверка числа на трехзначность
    if len(input_number) != 3:
        print("ОШИБКА! Введенное число не трехзначное.")
        return False
    
    # Переводим str (строку) в set (множество). Если длина множества равна 3, то высказывание истино
    tech_var = set(input_number)
    if len(tech_var) == 3:
        print(f"Все цифры {input_number} различны.")
    else:
        print(f"В {input_number} есть повторяющиеся цифры.")

# Функция для второго задания
def task_2():
    """
        Даны два числа.
        Вывести порядковый номер меньшего из них.
    """

    # Запрашиваем у пользователя числа и проверяем, являюся ли введенные значения числами
    # ("input_number_0: str = ..." означает, что переменная input_number ожидается строкой)
    input_number_0: str = input("Введите первое число: ")
    try:
        input_number_0 = float(input_number_0)
    except:
        print(f"ОШИБКА! {input_number_0} - не число.")
        return False

    input_number_1: str = input("Введите второе число: ")
    try:
        input_number_1 = float(input_number_1)
    except:
        print(f"ОШИБКА! {input_number_1} - не число.")
        return False

#     print(f"{input_number_0 if input_number_0 > input_number_1 else input_number_1} \
# больше {input_number_1 if input_number_1 < input_number_0 else input_number_0}"
#         if input_number_0 != input_number_1 else f"число {input_number_0} равно числу {input_number_1}")

    if input_number_0 < input_number_1:
        print("1 число меньше.")
    elif input_number_0 > input_number_1:
        print("2 число меньше.")
    elif input_number_0 == input_number_1:
        print("Числа равны.")
    
    

# Точка входа
if __name__ == "__main__":
    while True:
        main()