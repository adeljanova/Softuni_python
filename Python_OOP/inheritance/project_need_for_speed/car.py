from project_need_for_speed.vehicle import Vehicle


class Car(Vehicle):
    DEFAULT_FUEL_CONSUMPTION = 3

    def __init__(self, fuel: float, horse_power: int):
        super().__init__(fuel, horse_power)

    def drive(self, kilometers):
        fuel_needed = self.DEFAULT_FUEL_CONSUMPTION * kilometers
        if fuel_needed <= self.fuel:
            self.fuel -= fuel_needed