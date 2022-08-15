from project_zoo.animal import Animal


class Lion(Animal):
    money_to_be_cared = 50

    def __init__(self, name, gender, age):
        super().__init__(name, gender, age, self.money_to_be_cared)



