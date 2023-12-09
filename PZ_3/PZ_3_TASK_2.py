def main():
    """
    Negovora Nikita IS-25 Вариант 21

    2.
        Даны два числа.
        Вывести порядковый номер меньшего из них.
    """

    # Вызов функции для второго задания
    task_2()



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
        break_input = input("Продолжить? (y / n): ")
        if break_input.lower() == "n":
            break
        elif break_input.lower() == "y":
            print("Новый запуск")