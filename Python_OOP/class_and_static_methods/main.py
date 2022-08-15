from project.customer import Customer
from project.equipment import Equipment
from project.exercise_plan import ExercisePlan
from project.gym import Gym
from project.subscription import Subscription
from project.trainer import Trainer

customer = Customer("Aleksandra", "Atanas Manchev Street", "alja644@gmail.com")
equipment = Equipment("Dumbels")
trainer = Trainer("Vasil")
subscription = Subscription("21.07.2020", 1, 8, 12)
plan = ExercisePlan(3, 2, 11)

gym = Gym()

gym.add_customer(customer)
gym.add_equipment(equipment)
gym.add_trainer(trainer)
gym.add_plan(plan)
gym.add_subscription(subscription)

print(Customer.get_next_id())

print(gym.subscription_info(1))
