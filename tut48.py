# Map, Filter & Reduce

# 1. Map -------------------------------------------------------

# --- Not a convenient  way of converting a list items from string to int ----

# numbers = ["25", "26", "27"]
#
# for i in range(len(numbers)):
#     numbers[i] = int(numbers[i])
#
# numbers[2] = numbers[2] + 1
#
# print(numbers[2])


# we can do the above by using map

# print(type(map(int, numbers)))
# numbers = list(map(int, numbers))
# print(numbers)
#
# numbers[2] = numbers[2] + 1
#
# print(numbers[2])

# def sq(a):
#     return a*a
#
#
# num = [2, 3, 4, 5, 6, 7, 18, 9, 10]
# square = list(map(sq, num))
# print(square)

# num = [2, 3, 4, 5, 6, 7, 18, 9, 10]
# square = list(map(lambda x: x*x, num))
# print(square)


def square(a):
    return a*a


def cube(a):
    return a*a*a


func = [square, cube]

# for i in range(5):
#     val = list(map(lambda x: x(i), func))
#     print(val)

# 2. filter --------------------------------------------------------

# list1 = [1, 2, 3, 4, 5, 6, 7, 8, 9]
#
#
# def is_greater(num):
#     return num > 5
#
#
# greater_than = list(filter(is_greater, list1))
# print(greater_than);

# 3. Reduce --------------------------------------------------------

from functools import reduce

list1 = [1, 2, 3, 4, 5]

# num = 0
# for i in list1:
#     num = num + i
#     print(num, end=" ")

num = reduce(lambda x, y: x*y, list1)
print(num)
