from project_zoo.animal import Animal


class Tiger(Animal):
    money_to_be_cared = 45

    def __init__(self, name, gender, age):
        super().__init__(name, gender, age, self.money_to_be_cared)



