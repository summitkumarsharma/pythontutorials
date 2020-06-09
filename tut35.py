# Exercise 4 solution
# Pattern Printing
# Input = Integer n
# Boolean = True or False
#
# True n=5
# *
# **
# ***
# ****
#
# False n=5
# ****
# ***
# **
# *

# print("Pattern printing")
# choice = input("Enter your choice\n")
# num = int(input("Enter num how many rows you want :"))
# i = 1
# j = 1
# if choice == 1:
#     while i <= num:
#         while j <= i:
#             j = j + 1
#             print("*", end="")
#         print("\n")
#     i = i + 1
# else:
#     print("End of program")

# elif choice == 0:
#     while i < num:
#         print("*")
#         i = i + 1
# else:
# print("Bye, Thanks for visiting")


print("Pattern printing")
choice = int(input("Enter your choice\n"))
num = int(input("Enter num how many rows you want :\n"))
i = 1
j = 1
if choice == 1:
    for i in range(1, num):
        for j in range(i):
            print("*", end="")
        print("\n")
elif choice == 0:
    for i in range(num, 1):
        for j in range(i):
            print("*", end="")
        print("\n")
else:
    print("End")




