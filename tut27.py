# Execise 3 Quiz Solution
n=18
# Guess the number
# number of guess
# print the number
# print game over , you won
avail = 8
No_of_Guess = 1
print("Total Number of Guess Available = ", avail)
while No_of_Guess < 9:
    No_of_Guess = No_of_Guess + 1
    inp = int(input("Guess a Number-\n"))
    if inp == 18:
        No_of_Guess = No_of_Guess + 1
        avail = avail - 1
        print("You Won Congatulations \n")
        print("Number of attempt left to Guess = ", avail)
        break
    elif inp != 18 and No_of_Guess != 9:
        avail = avail - 1
        print("Number of Guess Available = ", avail)
        print("Guess Again:\n")
        continue
    elif No_of_Guess > 9:
        avail = avail - 1
        print("Number of Guess Available = ", avail)
        print("Game Over")
        break
    else:
        print("Game Over, you have no attempt left....")




