# Execise 3 Quiz
n=18
# Guess the number
# number of guess
# print the number
# print game over , you won

while 1:
    No_of_Guess = 9
    print("Total Number of Guess Available = ", No_of_Guess)
    inp = int(input("Guess a Number-\n"))
    if inp == 18:
        print("You Won Congatulations \n")
        print("Number of Guess = ", No_of_Guess)
        break
    elif inp != 18 and No_of_Guess != 9:
        No_of_Guess = No_of_Guess - 1
        print("Number of Guess Available = ", No_of_Guess)
        print("Guess Again:\n")
        continue
    elif No_of_Guess == 9:
        print("Number of Guess Available = ", No_of_Guess)
        print("Game Over")
        break
    else:
        print("Game Over")