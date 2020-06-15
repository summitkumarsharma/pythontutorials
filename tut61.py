# Multiple Inheritance


class Employee:
    no_of_leaves = 8
    var = 8

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


class Player:
    no_of_game = 4
    var = 9

    def __init__(self, name, game):
        self.name = name
        self.game = game

    def print_player_details(self):
        return f"The Name is {self.name}. He Played game {self.game}"


P1 = Player("Sam", ["Cricket", 'Football'])
# print(P1.print_player_details())


class CoolProgrammer(Employee, Player):
    language = "PHP"
    # var = 10

    def print_language(self):
        print(self.language)


C1 = CoolProgrammer("Jack", 9999, "CoolProgrammer")
det = C1.print_details()
print(det)

C1.print_language()
print(C1.var)