from project.car.car import Car


class MuscleCar(Car):
    MIN_SPEED_LIMIT = 250
    MAX_SPEED_LIMIT = 450

    def __init__(self, model, speed_limit):
        super().__init__(model, speed_limit)

    @property
    def min_speed_limit(self):
        return self.MIN_SPEED_LIMIT

    @property
    def max_speed_limit(self):
        return self.MAX_SPEED_LIMIT
