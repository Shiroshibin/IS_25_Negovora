"""
21. Создайте класс «Календарь», который имеет атрибуты год, месяц и день. Добавьте
методы для определения дня недели, проверки на високосный год и определения
количества дней в месяце
"""
import calendar
import re

class CALENDAR():
    def __init__(self, day = 15, month = 10, year = 2006) -> None:
        self.year = year
        self.month = month
        self.day = day
        self.day_name = {
            0: "Понедельник",
            1: "Вторник",
            2: "Среда",
            3: "Четверг",
            4: "Пятница",
            5: "Суббота",
            6: "Воскресенье"
        }

    def get_day_of_week(self):
        """
        Возвращает день недели на русском языке
        """
        day = calendar.weekday(self.year, self.month, self.day)
        day = self.day_name[day]
        return day
    
    def check_for_leap_year(self):
        """
        Возвращает строку "Весокосный" или "Не весокосный", по отношению к году, указаному в классе
        """
        result = calendar.isleap(self.year)
        if result: return "Весокосный"
        else: return "Не весокосный"

    def get_umber_of_days_in_a_month(self):
        """
        Возвращает строку "Дней в месяце: {data}", где date - количество дней в месяце 
        """
        data = calendar.monthrange(self.year, self.month)[1]
        return f"Дней в месяце: {data}"



if __name__ == "__main__":
    cal = CALENDAR()
    print(cal.get_day_of_week())
    print(cal.check_for_leap_year())
    print(cal.get_umber_of_days_in_a_month())