from project_wild_farm.customer import Customer
from project_wild_farm.equipment import Equipment
from project_wild_farm.exercise_plan import ExercisePlan
from project_wild_farm.subscription import Subscription
from project_wild_farm.trainer import Trainer


class Gym:

    def __init__(self):
        self.customers = []
        self.trainers = []
        self.equipments = []
        self.plans = []
        self.subscriptions = []

    def add_customer(self, customer: Customer):
        if customer not in self.customers:
            self.customers.append(customer)

    def add_equipment(self, equipment: Equipment):
        if equipment not in self.equipments:
            self.equipments.append(equipment)

    def add_plan(self, plan: ExercisePlan):
        if plan not in self.plans:
            self.plans.append(plan)

    def add_subscription(self, subscription: Subscription):
        if subscription not in self.subscriptions:
            self.subscriptions.append(subscription)

    def add_trainer(self, trainer: Trainer):
        if trainer not in self.trainers:
            self.trainers.append(trainer)

    def subscription_info(self, subscription_id: int):
        subscription = self.__get_by_id(subscription_id, self.subscriptions)
        if type(subscription) is None:
            return
        else:
            customer = self.__get_by_id(subscription.customer_id, self.customers)
            trainer = self.__get_by_id(subscription.trainer_id, self.trainers)
            exercise_plan = self.__get_by_id(subscription.exercise_id, self.plans)
        if type(exercise_plan) is None:
            return
        else:
            equipment = self.__get_by_id(exercise_plan.equipment_id, self.equipments)
        result = ''
        if self.subscriptions:
            result += repr(subscription) + '\n'
        if self.customers:
            result += repr(customer) + '\n'
        if self.trainers:
            result += repr(trainer) + '\n'
        if self.equipments:
            result += repr(equipment) + '\n'
        if self.plans:
            result += repr(exercise_plan) + '\n'

        return result.strip()

    def __get_by_id(self, id_number, list_of_ids):
        for id in list_of_ids:
            if id.id == id_number:
                return id