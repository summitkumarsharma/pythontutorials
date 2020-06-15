# Single Inheritance


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
        print("This is good " + string)


class Programmer(Employee):
    no_of_holidays = 56

    def __init__(self, a_name, a_salary, a_role, a_languages):
        self.name = a_name
        self.salary = a_salary
        self.role = a_role
        self.languages = a_languages

    def print_programmer_details(self):
        return f"The Programmer's Name is {self.name}. Salary is {self.salary} .role is {self.role} and " \
               f"Languages are-{self.languages}"


emp1 = Employee("John", 25, "Instructor")
emp2 = Programmer("Alex", 24, "Programmer", ['python', 'php'])

print(emp2.print_programmer_details())
print(emp2.print_details())
print(emp2.no_of_holidays)
