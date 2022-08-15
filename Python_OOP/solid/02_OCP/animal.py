import os


class Cat:
    def __init__(self, sound: str):
        self.sound = sound

    @staticmethod
    def animal_sound():
        return 'meow'


class Dog:
    def __init__(self, sound: str):
        self.sound = sound

    @staticmethod
    def animal_sound():
        return 'woof-woof'


class Cow:
    def __init__(self, sound: str):
        self.sound = sound

    @staticmethod
    def animal_sound():
        return 'moo'


class Animal:
    def __init__(self, species):
        self.species = species

    def animal_sound(self):
        return sum(sp.animal_sound() for sp in self.species)


# class StdPrinter:
#     def print(self, obj):
#         print(obj)
#
#
# class FilePrinter:
#     def __init__(self, filename):
#         self.filename = filename
#
#     def print(self, obj):
#         with open(self.filename, 'a') as file:
#             file.write(str(obj))
#             file.write(os.linesep)


# printer = StdPrinter()
animal1 = Animal('cat')
animal2 = Animal('dog')
animal3 = Animal('cow')
animal_list = Animal([animal1, animal2, animal3])
animals = [animal1, animal2, animal3, animal_list]
[print(sp.animal_sound()) for sp in animals]



## добавете ново животно и рефакторирайте кода да работи без да се налага да се правят промени по него
## при добавяне на нови животни
# animals = [Animal('cat'), Animal('dog'), Animal('chicken')]
