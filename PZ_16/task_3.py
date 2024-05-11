"""
Для задачи из блока 1 создать две функции, save_def и load_def, которые позволяют
сохранять информацию из экземпляров класса в файл и загружать ее обратно.
Использовать модуль pickle для сериализации и десериализации объектов Python в
бинарном формате.
"""
import pickle

from task_1 import CALENDAR as OLD_CALENDAR
from task_2 import DOG as OLD_DOG

class CALENDAR(OLD_CALENDAR):
    def __init__(self, day=15, month=10, year=2006):
        super().__init__(day, month, year)

class DOG(OLD_DOG):
    def __init__(self, kind="Собака", number_of_paws=4, color="Белый", name="Боб", breed="Дворняга"):
        super().__init__(kind, number_of_paws, color, name, breed)

def save_def(obj: object):
    with open(f"{obj.__class__.__name__}.pickle", "wb") as file:
        pickle.dump(obj, file)

def load_def(class_name):
    with open(f"{class_name}.pickle", "rb") as file:
        result = pickle.load(file)
    return result

if __name__ == "__main__":
    save_def(DOG(name="Игорь"))
    igor = load_def("DOG")
    igor_description = igor.get_all_attribute()
    print(*igor_description, sep="\n")