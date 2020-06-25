# Object Introspection

# Setters,deleter & Property Decorators


class Employee:
    def __init__(self, f_name, l_name):
        self.f_name = f_name
        self.l_name = l_name
        # self.email = f"{f_name}.{l_name}@g_mail.com"

    def explain(self):
        return f"The Employee is {self.f_name} {self.l_name}"

    def print_email(self):
        pass

    @property
    def my_email(self):
        if self.f_name == None or self.l_name == None:
            return "Email is not set....please set email"
        else:
            return f"{self.f_name}.{self.l_name}@gmail.com"

    @my_email.setter
    def my_email(self, string):
        print("Setting now....")
        names = string.split("@")[0]
        self.f_name = names.split(".")[0]
        self.l_name = names.split(".")[1]

    @my_email.deleter
    def my_email(self):
        self.f_name = None
        self.l_name = None


emp1 = Employee("Pokemon", "Ninja")
# print(emp1.my_email)
# print(type(emp1))
# print(type("This is String..."))
# print(id("This is String..."))
# print(id("This is String.2.."))

# print(dir("This is String..."))
# print(dir(emp1))

import inspect
print(inspect.getmembers(emp1))
