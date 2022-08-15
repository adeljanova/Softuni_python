from abc import ABC, abstractmethod


class Horse(ABC):
    MIN_LEN = 4

    def __init__(self, name: str, speed: int):
        self.name = name
        self.speed = speed
        self.is_taken = False

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        if len(value) < self.MIN_LEN:
            raise ValueError(f"Horse name {value} is less than {self.MIN_LEN} symbols!")
        self.__name = value

    @property
    def speed(self):
        return self.__speed

    @speed.setter
    def speed(self, value):
        if value > self.max_speed:
            raise ValueError("Horse speed is too high!")
        self.__speed = value

    @property
    @abstractmethod
    def max_speed(self):
        pass

    @abstractmethod
    def train(self):
        pass


