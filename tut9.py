# List Data type ---it is mutable = use symbol []
grocery = ["Harpic", "vim bar", "deodrant", "Bhindi",
           "Lollypop", 56]
print(grocery)
print(grocery[5])
numbers = [2, 7, 9, 11, 3]
print(numbers)

# list Methods

# numbers.remove(9)
# numbers.pop()
# numbers.sort()
# numbers = []
# numbers.reverse()
numbers.append(1)
numbers.append(72)
numbers.append(5)
numbers.insert(2, 67)
print(numbers)
# 3, 11, 9, 7, 2
# print(numbers)
# numbers[1] = 98
# print(numbers)

# Mutable - can change
# Immutable - cannot change

# Tuple -- It is Immutable data type use symbol -()

tp = (1, 2, 3, 4)
print(tp)

# Program to Swap two numbers

a = 1
b = 8
print("Before Swapping")

print(a,b)
a, b = b, a
# temp = a
# a = b
# b = temp

print("After Swapping")
print(a, b)