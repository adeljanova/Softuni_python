from project.car.car import Car
from project.driver import Driver
from project.race import Race


class Controller:

    def __init__(self):
        self.cars = []
        self.drivers = []
        self.races = []

    def create_car(self, car_type: str, model: str, speed_limit: int):
        if car_type != "MuscleCar" or car_type != "SportsCar":
            return
        car = Car(model, speed_limit)
        if car.is_taken:
            raise Exception(f"Car {model} is already created!")
        self.cars.append(car)
        return f"{car_type} {model} is created."

    def create_driver(self, driver_name: str):
        driver = Driver(driver_name)
        if driver.name in self.drivers:
            raise Exception(f"Driver {driver_name} is already created!")

        self.drivers.append(driver)
        return f"Driver {driver_name} is created."

    def create_race(self, race_name: str):
        race = Race(race_name)
        if race.name in self.races:
            raise Exception(f"Race {race_name} is already created!")

        self.races.append(race)
        return f"Race {race_name} is created."

    def add_car_to_driver(self, driver_name: str, car_type: str):
        driver = self.__find_driver_by_name(driver_name)
        if driver is None:
            raise Exception(f"Driver {driver_name} could not be found!")

        car = self.__find_last_free_car_by_type(car_type)
        if car is None:
            raise Exception(f"Car {car_type} could not be found!")

    def add_driver_to_race(self, race_name: str, driver_name: str):
        pass

    def start_race(self, race_name: str):
        pass

    def __find_driver_by_name(self, driver_name):
        for driver in self.drivers:
            if driver.name == driver_name:
                return driver
            return None

    def __find_last_free_car_by_type(self, car_type):
        for idx in range(len(self.cars) - 1, -1, -1):
            car = self.cars[idx]
            if car.is_taken and car.__class__.__name__ == car_type:
                return car
        return None
