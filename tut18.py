# Break and Continue
i = 0
while i < 25:
    if i < 5:
        i = i + 1
        continue
    print("i=", i+1)
    if i == 19:
        break
    i = i + 1


# Quiz

while 1:
    inp = int(input("Enter a Number-\n"))
    if inp > 100:
        print("Congrats you have entered number Greater than 100\n")
        break
    else:
        print("Try Again:\n")
        continue