from project_zoo.animal import Animal
from project_zoo.caretaker import Caretaker
from project_zoo.cheetah import Cheetah
from project_zoo.keeper import Keeper
from project_zoo.lion import Lion
from project_zoo.tiger import Tiger
from project_zoo.vet import Vet
from project_zoo.worker import Worker


class Zoo:

    def __init__(self, name: str, budget: int, animal_capacity: int, workers_capacity: int):
        self.name = name
        self.__budget = budget
        self.__animal_capacity = animal_capacity
        self.__workers_capacity = workers_capacity
        self.animals = []
        self.workers = []

    def add_animal(self, animal: Animal, price):
        if self.__animal_capacity == len(self.animals):
            return "Not enough space for animal"
        if price > self.__budget:
            return "Not enough budget"
        self.animals.append(animal)
        self.__budget -= price
        return f"{animal.name} the {animal.__class__.__name__} added to the zoo"

    def hire_worker(self, worker: Worker):
        if self.__workers_capacity == len(self.workers):
            return "Not enough space for worker"
        self.workers.append(worker)
        return f"{worker.name} the {worker.__class__.__name__} hired successfully"

    def fire_worker(self, worker_name):
        for worker in self.workers:
            if worker.name == worker_name:
                self.workers.remove(worker)
                return f"{worker_name} fired successfully"
        return f"There is no {worker_name} in the zoo"

    def pay_workers(self):
        sum_of_salaries = 0
        for worker in self.workers:
            sum_of_salaries += worker.salary
        if self.__budget >= sum_of_salaries:
            self.__budget -= sum_of_salaries
            return f"You payed your workers. They are happy. Budget left: {self.__budget}"
        return "You have no budget to pay your workers. They are unhappy"

    def tend_animals(self):
        sum_of_money_care = 0
        for animal in self.animals:
            sum_of_money_care += animal.money_for_care
        if self.__budget >= sum_of_money_care:
            self.__budget -= sum_of_money_care
            return f"You tended all the animals. They are happy. Budget left: {self.__budget}"
        return "You have no budget to tend the animals. They are unhappy."

    def profit(self, amount):
        self.__budget += amount

    def animals_status(self):
        result = f"You have {len(self.animals)} animals\n"
        lions = [repr(a) for a in self.animals if isinstance(a, Lion)]
        result += f"----- {len(lions)} Lions:\n" + '\n'.join(lions) + '\n'
        tigers = [repr(a) for a in self.animals if isinstance(a, Tiger)]
        result += f"----- {len(tigers)} Tigers:\n" + '\n'.join(tigers) + '\n'
        cheetahs = [repr(a) for a in self.animals if isinstance(a, Cheetah)]
        result += f"----- {len(cheetahs)} Cheetahs:\n" + '\n'.join(cheetahs) + '\n'
        return result.strip()

    def workers_status(self):
        result = f"You have {len(self.workers)} workers\n"
        keepers = [repr(w) for w in self.workers if isinstance(w, Keeper)]
        result += f"----- {len(keepers)} Keepers:\n" + '\n'.join(keepers) + '\n'
        caretakers = [repr(w) for w in self.workers if isinstance(w, Caretaker)]
        result += f"----- {len(caretakers)} Caretakers:\n" + '\n'.join(caretakers) + '\n'
        vets = [repr(w) for w in self.workers if isinstance(w, Vet)]
        result += f"----- {len(vets)} Vets:\n" + '\n'.join(vets) + '\n'
        return result.strip()
