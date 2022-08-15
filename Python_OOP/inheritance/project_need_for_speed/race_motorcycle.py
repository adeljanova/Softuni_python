from project_need_for_speed.motorcycle import Motorcycle


class RaceMotorcycle(Motorcycle):
    DEFAULT_FUEL_CONSUMPTION = 8

    def __init__(self, fuel: float, horse_power: int):
        super().__init__(fuel, horse_power)

    def drive(self, kilometers):
        fuel_needed = self.DEFAULT_FUEL_CONSUMPTION * kilometers
        if fuel_needed <= self.fuel:
            self.fuel -= fuel_needed
