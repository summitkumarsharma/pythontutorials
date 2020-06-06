# scope of variables

# l = 10                  # Global

# def function_1(n):
#     # l = 5             # Local
#     m = 8               # Local
#     global l
#     l = l + 45
#     print(l, m)
#     print(n, "I have printed")
#
#
# function_1("This is me")
# print(l)
# print(m)

x = 89


def f1():
    x = 20

    def f2():
        global x
        x = 88

    print("before calling f2()", x)
    f2()
    print("after calling f2()", x)


f1()
print(x)
