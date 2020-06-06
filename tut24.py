# Exception handling

print("Enter the number 1")
num1 = input()
print("Enter the number 2")
num2 = input()
try:
    print("The sum of two numbers is=", int(num1) + int(num2))
except Exception as e:
    print(e)

print("This ia an important line")