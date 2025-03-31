import random


while True:
    guess_number = random.randint(1, 100)
    option = int(input("Guess a number between 1 and 100 with the fewest guesses: "))

    if option > guess_number:
        print("Too high. Try again.")
    else:
        print("Too low. Try again.")

    if option == guess_number:
        print("Congratulations. You guessed the number" + str(guess_number))
        break

    user_option = str(input("Would you like to play again? (y/n): "))
    if user_option == "n":
        break
    else:
        continue
