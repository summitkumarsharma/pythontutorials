# Decorators In Python

# 1. Working of a Normal Function ------------------------------------------------------
# def function1():
#     print("Decorators In Python")


# func2 = function1
# del function1
# func2()
# print(func2())

#  2. A function can return function also-----------------------------------------------


# def func_ret(num):
#     if num == 0:
#         return print
#     if num == 1:
#         return sum


# a = func_ret(0)
# print(a)
# a = func_ret(1)
# print(a)

# def executor(func):
#     func("Passing function name as an argument")
#
#
# executor(print)


# 3. A Function name can be passed as an argument in a function can return a function  using decorator ---

def dec1(func1):
    def now_exec():
        print("Executing now")
        func1()
        print("Executed")
    return now_exec


@dec1
def greet():
    print("Good Morning")


# greet = dec1(greet) # we cn skip this step and can do using decorator---
greet()
