"""
21. Создайте базовый класс "Животное" со свойствами "вид", "количество лап", "цвет
шерсти". От этого класса унаследуйте класс "Собака" и добавьте в него свойства
"кличка" и "порода". 
"""

from typing import Any


class ANIMAL():
    def __init__(self, kind = "Животное", number_of_paws = 4, color = "Белый"):
        self.kind = kind 
        self.number_of_paws = number_of_paws
        self.color = color

class DOG(ANIMAL):
    def __init__(self, kind="Собака", number_of_paws=4, color="Белый", name="Боб", breed="Дворняга"):
        super().__init__(kind, number_of_paws, color)
        self.name = name
        self.breed = breed

    def get_all_attribute(self) -> list[str]:
        list_attr = [attr for attr in self.__dict__ if not callable(getattr(self, attr)) and not attr.startswith("__")]
        list_attr = [f"  {item}: {self.__getattribute__(item)}" for item in list_attr]
        return list_attr

if __name__ == "__main__":
    bob = DOG(name="Боб", breed="Немецкая Гончая")
    bob_description = bob.get_all_attribute()
    print("\nОписание Боба:")
    print(*bob_description, sep="\n")
    print("\n")