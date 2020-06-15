# Public, Private & Protected Access Specifiers


class Employee:
    no_of_leaves = 8
    var = 8
    _protec = 9
    __private = 98

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


emp1 = Employee("John", 25, "Instructor")
emp2 = Employee("Alex", 24, "Programmer")

print(emp1._protec)
print(emp1._Employee__private)      # name mangling
