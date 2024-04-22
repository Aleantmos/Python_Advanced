from _3_MultipleInheritance.employee import Employee
from _3_MultipleInheritance.person import Person


class Teacher(Person, Employee):
    def teach(self):
        return "teaching..."
