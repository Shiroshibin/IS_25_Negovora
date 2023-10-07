# Объявление функции
def main(number = ""):

    """Чтение трехзначного числа справа налево"""

    # Проверка количестива символов
    try:
        if len(number) != 3:
            return "На ввод принимается только 3 символа"
    except:
        return "На ввод принимается только 3 символа"

    # Проверка, является ли input числом
    try:
        int(number)
    except:
        return "Вы ввели не целое число, попробуйте снова"

    # Перевод input в список и разворот списка через срезы
    number_list = list(number)[::-1]

    # Преобразование списка в строку
    answer = ""
    for i in number_list:
        answer += i
    #
    return answer


# Точка входа
if __name__ == '__main__':
    # Запрос данных и вызов функции
    number = input("Введите любое трехзначное целое число: ")
    print(f"Вот это число, но развернутое справа на лево   {main(number)}")
