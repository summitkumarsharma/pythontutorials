# Abstraction & Encapsulation


class Employee:
    no_of_leaves = 8

    def __init__(self, a_name, a_salary, a_role):
        self.name = a_name
        self.salary = a_salary
        self.role = a_role

    def print_details(self):
        return f"The Name is {self.name}. Salary is {self.salary} and role is {self.role}"

    @classmethod
    def change_leaves(cls, new_leaves):
        cls.no_of_leaves = new_leaves

    @classmethod
    def from_dash(cls, string):
        return cls(*string.split("-"))

    @staticmethod
    def print_good(string):
        print("This is good ", string)


e1 = Employee("Harry", 255, "Instructor")
e2 = Employee("Rohan", 455, "Student")
e3 = Employee.from_dash("Karan-480-Student")

Employee.print_good("Rohan")


