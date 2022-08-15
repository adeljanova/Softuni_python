from abc import ABC, abstractmethod


class Vehicle(ABC):

    def __init__(self, fuel_quantity, fuel_consumption):
        self.fuel_quantity = fuel_quantity
        self.fuel_consumption = fuel_consumption

    @abstractmethod
    def drive(self, distance):
        pass

    @abstractmethod
    def refuel(self, fuel):
        pass


class Car(Vehicle):
    AIR_CONDITIONER = 0.9

    def __init__(self, fuel_quantity, fuel_consumption):
        super().__init__(fuel_quantity, fuel_consumption)

    def drive(self, distance):
        self.fuel_consumption += self.AIR_CONDITIONER
        trip_consumption = distance * self.fuel_consumption
        if trip_consumption < self.fuel_quantity:
            self.fuel_quantity -= trip_consumption

    def refuel(self, fuel):
        self.fuel_quantity += fuel
        return self.fuel_quantity


class Truck(Vehicle):
    AIR_CONDITIONER = 1.6

    def __init__(self, fuel_quantity, fuel_consumption):
        super().__init__(fuel_quantity, fuel_consumption)

    def drive(self, distance):
        self.fuel_consumption += self.AIR_CONDITIONER
        trip_consumption = distance * self.fuel_consumption
        if trip_consumption < self.fuel_quantity:
            self.fuel_quantity -= trip_consumption
            return self.fuel_quantity

    def refuel(self, fuel):
        self.fuel_quantity += (fuel * 0.95)
        return self.fuel_quantity


car = Car(20, 5)
car.drive(3)
print(car.fuel_quantity)
car.refuel(10)
print(car.fuel_quantity)
truck = Truck(100, 15)
truck.drive(5)
print(truck.fuel_quantity)
truck.refuel(50)
print(truck.fuel_quantity)

