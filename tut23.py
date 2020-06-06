# Functions in python

a = 7
b = 8
c = sum((a, b))    # built in functions
# print(c)


# user defined function

def function1():
    print("we are in function 1")


# print(function1())
# function1()

def function2(a, b):
    print("sum of a and b", a+b)

# function2(2, 6)


def function3(a, b):
    """This is a function which will calculate average of two numbers"""
    average = (a+b)/2
    # print("average =", average)
    return average


v = function3(2, 6)
print("Average =", v)

print(function3.__doc__)