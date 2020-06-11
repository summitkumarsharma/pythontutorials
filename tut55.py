# Self & __init__() (Constructors)


class Employee:
    no_of_leaves = 8      # class variables

    def __init__(self, name, salary, role):             # defining class constructors
        self.name = name
        self.salary = salary
        self.role = role

    def print_details(self):                            # defining display constructor methods
        return f"Name is {self.name} , Salary is {self.salary} and Role is {self.role}"


# emp1 = Employee()         # object of Employee class
# emp2 = Employee()

# creating instance variables of  object emp1
# emp1.name = "John"
# emp1.salary = 25
# emp1.role = "Instructor"

# creating instance variables of  object emp2
# emp2.name = "Alex"
# emp2.salary = 24
# emp2.role = "Programmer"

# print(emp1.print_details())
# print(emp2.print_details())

# using constructors
emp1 = Employee("John", 25, "Instructor")
emp2 = Employee("Alex", 24, "Programmer")
print(emp1.print_details())
print(emp2.print_details())
print(emp1.__dict__)
print(emp2.__dict__)

