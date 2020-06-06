# Exercise 2 - Faulty Calculator
# 45 * 3 = 555, 56+9 = 77, 56/6 = 4
# Design a calculator which will correctly solve all the problems except
# the following ones:
# 45 * 3 = 555, 56+9 = 77, 56/6 = 4
# Your program should take operator  and the two numbers as input from the user
# and then return the result

operand1 = int(input("Enter the first Number\n"))
operand2 = int(input("Enter the Second Number\n"))
operator = input("Enter the Operator-\n")

if operator == "+":
    if operand1 == 56 and operand2 == 9:
        a = 77
        print("Sum =", a)
    else:
        print("Sum =", operand1+operand2)
elif operator == "-":
    if operand1 == 45 and operand2 == 3:
        a = 52
        print("Sum =", a)
    else:
        print("Difference =", operand1 - operand2)
elif operator == "*":
    if operand1 == 45 and operand2 == 3:
        a = 555
        print("Multiply =", a)
    else:
        print("Multiply =", operand1 * operand2)
elif operator == "/":
    if operand1 == 56 and operand2 == 6:
        a = 4
        print("Division =", a)
    else:
        print("Division =", operand1 / operand2)
else:
    print("Thank you")