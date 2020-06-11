# Instance & Class Variables


class Employee:
    no_of_leaves = 8     # class variables
    pass


emp1 = Employee()         # object of Employee class
emp2 = Employee()

# creating instance variables of  object emp1
emp1.name = "John"
emp1.salary = 25
emp1.role = "Instructor"

# creating instance variables of  object emp2
emp2.name = "Alex"
emp2.salary = 24
emp2.role = "Programmer"

print(emp1.name)
print(emp1.no_of_leaves)

# print object emp1 and emp2 using dict
print(emp1.__dict__)
print(emp2.__dict__)


emp1.no_of_leaves = 5
print(emp1.__dict__)
print(emp1.no_of_leaves)

Employee.no_of_leaves = 9
print(Employee.no_of_leaves)

print(Employee.__dict__)