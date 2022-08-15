from project_multiple_inheritance.employee import Employee
from project_multiple_inheritance.person import Person


class Teacher(Person, Employee):

    def teach(self):
        return "teaching..."


