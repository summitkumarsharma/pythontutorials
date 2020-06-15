# Diamond Shape Problem In Multiple Inheritance


class A:

    def my_print(self):
        print("This is a method in class A")


class B(A):
    def my_print(self):
        print("This is a method in class B")


class C(A):
    def my_print(self):
        print("This is a method in class C")


class D(B, C):
    def my_print(self):
        print("This is a method in class D")


a = A()
b = B()
c = C()
d = D()

d.my_print()
