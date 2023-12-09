def main():
    """
    Negovora Nikita IS-25 Вариант 21

    2. 
        Дано целое число N (>0). 
        Если оно является степенью числа 3, то вывести TRUE,
        если не является — вывести FALSE.
    """

    # Вызов функции для второго задания
    task_2()
    

# Функция для второго задания
def task_2():
    """
        Дано целое число N (>0). 
        Если оно является степенью числа 3, то вывести TRUE,
        если не является — вывести FALSE.
    """
    # Запрашиваем у пользователя число N (N > 0)
    # Так же выполняем его проверку на  N > 0
    try:
        input_number_N: int = int(input("Введите целое число N (N > 0): "))
    except:
        print("Введено не целое число.")
        return False

    if input_number_N <= 0:
        print("Не соблюдено условие N > 0.")
        return False
    
    # Пока N > 3, делим N на 3 и присваем ей результат деления 
    while input_number_N > 3:
        input_number_N = input_number_N / 3
        
    # Если N равен 3, значит N состоит из перемноженных несколько раз 3, а значит N - степень 3
    if input_number_N == 3:
        print("TRUE")
        return True
    else:
        print("FALSE") 
        return False   
    
            
        
        
    
    

# Точка входа
if __name__ == "__main__":
    while True:
        main()