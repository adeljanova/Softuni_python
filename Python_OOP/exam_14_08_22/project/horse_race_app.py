from project.horse_race import HorseRace
from project.horse_specification.appaloosa import Appaloosa
from project.horse_specification.thoroughbred import Thoroughbred
from project.jockey import Jockey


class HorseRaceApp:
    VALID_TYPES_HORSES = ["Appaloosa", "Thoroughbred"]
    VALID_TYPES_RACES = ["Winter", "Spring", "Autumn", "Summer"]

    def __init__(self):
        self.horses = []
        self.jockeys = []
        self.horse_races = []

    def add_horse(self, horse_type: str, horse_name: str, horse_speed: int):
        horse = Appaloosa(horse_name, horse_speed) if horse_type == "Appaloosa" \
            else Thoroughbred(horse_name, horse_speed)
        if horse_type not in self.VALID_TYPES_HORSES:
            return

        for h in self.horses:
            if h.name == horse.name:
                raise Exception(f"Horse {horse_name} has been already added!")
        self.horses.append(horse)
        return f"{horse_type} horse {horse_name} is added."

    def add_jockey(self, jockey_name: str, age: int):
        jockey = Jockey(jockey_name, age)
        for j in self.jockeys:
            if j.name == jockey.name:
                raise Exception(f"Jockey {jockey_name} has been already added!")
        self.jockeys.append(jockey)
        return f"Jockey {jockey_name} is added."

    def create_horse_race(self, race_type: str):
        race = HorseRace(race_type)
        for r in self.horse_races:
            if r.race_type == race.race_type:
                raise Exception(f"Race {race.race_type} has been already created!")
        self.horse_races.append(race)
        return f"Race {race.race_type} is created."

    def add_horse_to_jockey(self, jockey_name: str, horse_type: str):
        jockey = self.__find_jockey_by_name(jockey_name)
        horse = self.__find_horse_by_type(horse_type)
        if jockey is None:
            raise Exception(f"Jockey {jockey_name} could not be found!")
        if horse is None:
            raise Exception(f"Horse breed {horse_type} could not be found!")
        if jockey.horse is not None and jockey.horse.is_taken:
            return f"Jockey {jockey_name} already has a horse."

        jockey.horse = horse
        jockey.horse.is_taken = True
        return f"Jockey {jockey_name} will ride the horse {horse.name}."

    def add_jockey_to_horse_race(self, race_type: str, jockey_name: str):
        jockey = self.__find_jockey_by_name(jockey_name)
        race = self.__find_race_by_type(race_type)
        if race not in self.horse_races:
            raise Exception(f"Race {race_type} could not be found!")
        if jockey not in self.jockeys:
            raise Exception(f"Jockey {jockey_name} could not be found!")
        if jockey in self.jockeys and jockey.horse is None:
            raise Exception(f"Jockey {jockey_name} cannot race without a horse!")
        if jockey in race.jockeys:
            return f"Jockey {jockey_name} has been already added to the {race_type} race."

        race.jockeys.append(jockey)
        return f"Jockey {jockey_name} added to the {race_type} race."

    def start_horse_race(self, race_type: str):
        race = self.__find_race_by_type(race_type)
        if race not in self.horse_races:
            raise Exception(f"Race {race_type} could not be found!")
        if len(self.jockeys) < 2:
            raise Exception(f"Horse race {race_type} needs at least two participants!")

        winner = ''
        max_speed = 0
        for jockey in self.jockeys:
            if jockey.horse.speed > max_speed:
                max_speed = jockey.horse.speed
                winner = jockey
        return f"The winner of the {race_type} race, with a speed of " \
               f"{max_speed}km/h is {winner.name}! Winner's horse: {winner.horse.name}."

    def __find_jockey_by_name(self, jockey_name):
        for jockey in self.jockeys:
            if jockey.name == jockey_name:
                return jockey
        return None

    def __find_horse_by_type(self, horse_type):
        for idx in range(len(self.horses) - 1, -1, -1):
            horse = self.horses[idx]
            if horse.__class__.__name__ == horse_type:
                return horse
        return None

    def __find_race_by_type(self, race_type):
        for race in self.horse_races:
            if race.race_type == race_type:
                return race
        return None
