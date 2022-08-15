from project_zoo.animal import Animal


class Cheetah(Animal):
    money_to_be_cared = 60

    def __init__(self, name, gender, age):
        super().__init__(name, gender, age, self.money_to_be_cared)


