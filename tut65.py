# Super() and Overriding In Classes
class A:
    class_var1 = "I am a class variable in class A"

    def __init__(self):
        self.var1 = "I am inside  class A constructor"
        self.class_var1 = "I am an instance variable in class A"
        self.special = "special"


class B(A):
    # class_var1 = "I am a class variable in class B"

    def __init__(self):
        # super().__init__()
        self.var1 = "I am inside  class B constructor"
        self.class_var1 = "I am an instance variable in class B"
        super().__init__()


a = A()
b = B()
print(b.class_var1)
print(b.special, b.var1, b.class_var1)
