import math

def main():
    """
    Negovora Nikita IS-25 Вариант 21

    1. 
        Составить функцию, которая выполнит суммирования числового ряда.
    2. 
        Описать функцию Power1(A, B) вещественного типа, 
        находящую величину AB поформуле AB = exp(B*ln(A)) (параметры A и B — вещественные). 
        В случае нулевого или отрицательного параметра A функция возвращает 0. 
        С помощью этой функции найти степени AP, BP, CP, если даны числа P, A, B, C.
    """

    # Вызов функции для первого задания
    # task_1()

    # Вызов функции для второго задания
    # Power1(99, 2)

    # Вызов функции для второго задания
    task_2_1()

    

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



# Функция для второго задания
def Power1(A: float, B: float):
    """
        Описать функцию Power1(A, B) вещественного типа, 
        находящую величину AB поформуле AB = exp(B*ln(A)) (параметры A и B — вещественные). 
        В случае нулевого или отрицательного параметра A функция возвращает 0. 
        С помощью этой функции найти степени A^P, B^P, C^P, если даны числа P, A, B, C.
    """

    # Проверка типа данных
    try:
        A = float(A)
        B = float(B)
    except:
        print("Переданы неверные данные.")
        return False
    
    # Проверка данных на положительность
    if A <= 0 or B <= 0:
        print(0)
        return 0
     
    # С помощью стандартной библиотеки math для математ действий считаем значение AB и выводим его 
    AB = math.exp(B * math.log(A, math.e))
    print(AB)
    return AB
    
def task_2_1():

    """
        С помощью Power1() найти степени A^P, B^P, C^P, если даны числа P, A, B, C.
    """

    A : str = input("Введите число A: ")
    B : str = input("Введите число B: ")
    C : str = input("Введите число C: ")
    P : str = input("Введите число P: ")

    print(
        f"Power1({A}, {P}) = {Power1(A, P)}\n\
Power1({B}, {P}) = {Power1(B, P)}\n\
Power1({C}, {P}) = {Power1(C, P)}"
    )
    
        

# Точка входа
if __name__ == "__main__":
    while True:
        main()
    