import math

def main():
    """
    Negovora Nikita IS-25 Вариант 21

    1. 
        Составить функцию, которая выполнит суммирования числового ряда.
    """

    # Вызов функции для первого задания
    task_1()



# Функция для первого задания
def task_1():
    """
        Составить функцию, которая выполнит суммирования числового ряда.
    """

    # Запрос данных
    input_data: str = input('Введите числа через запятую (Пример - "0, 1, 2"): ')
    
    # Создание списка через экземпляр класса 
    data_list = list()

    # Перевод str в int через .split() по разделяющему символу и int() c последующим добавлением в list
    try:
        for i in input_data.split(","):
            # На случай, если ряд заканчивается запятой
            if i != "":
                data_list.append(int(i))
    # Обработчик ошибок. Ловит ошибки .split() и int()
    except:
        print("Ряд введен не коректно")
        return False
    
    # Вывод результата работы функции
    print(sum(data_list))
    return(sum(data_list))



# Точка входа
if __name__ == "__main__":
    while True:
        main()
        break_input = input("Продолжить? (y / n): ")
        if break_input.lower() == "n":
            break
        elif break_input.lower() == "y":
            print("Новый запуск")
    