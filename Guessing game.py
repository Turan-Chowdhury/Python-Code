from random import randint

for x in range(5):
    guessNumber = int(input("Enter your guess between 1 and 5 : "))
    randomNumber = randint(1, 5)

    if guessNumber == randomNumber:
        print("you have won!")
    else:
        print("you have lost")
        print("Random number was :", randomNumber)
