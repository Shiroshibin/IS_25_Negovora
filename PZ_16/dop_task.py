class Note:
    def __init__(self, iscompleted = False, count = 0) -> None:
        self.iscompleted = iscompleted
        self.count = count
    def up_count(self, digit = 0):
        self.count += 1 
        return self.count
    def reset_count(self):
        self.count = 0

note = Note(True)
# print(f"{note.__dict__=}")
# print(f"{Note.__dict__=}\n")


# note.up_count(5)
# print(f"{note.__dict__=}")
# print(f"{Note.__dict__=}\n")

# note.reset_count()
# print(f"{note.__dict__=}")
# print(f"{Note.__dict__=}\n")

class Image:
    def __init__(self, resolution = "", title = "", extension = "", size = (1, 1)) -> None:
        self.resolution = resolution
        self.title = title
        self.extension = extension
        self.size = size

    def resize(self, size = (2, 2)):
        self.size = size
        print(f"{self.size=}")

    def title_upper(self):
        self.title = self.title.capitalize()

# img_1 = Image()
# img_1.resize((5, 5))
# img_2 = Image()
# img_2.resize((4, 4))


class Person:
    count = 0
    def __init__(self, name) -> None:
        self.name = name
        Person.count += 1

    @staticmethod
    def total_peope():
        return f"Создано {Person.count} объектов"
    
# bob = Person("Bob")
# igor = Person("Igor")
# print(Person.total_peope())
