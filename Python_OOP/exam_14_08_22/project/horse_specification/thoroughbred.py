from project.horse_specification.horse import Horse


class Thoroughbred(Horse):
    MAX_SPEED = 140
    SPEED_INCREMENT = 3

    def __init__(self, name: str, speed: int):
        super().__init__(name, speed)

    @property
    def max_speed(self):
        return self.MAX_SPEED

    def train(self):
        self.speed += self.SPEED_INCREMENT
        if self.speed >= self.MAX_SPEED:
            self.speed = self.MAX_SPEED
            return self.speed
