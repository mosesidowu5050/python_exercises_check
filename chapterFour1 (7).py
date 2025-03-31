import random


while True:
  count = 0
  while True:
    guess_number = random.randint(1, 100)
    option = int(input("Guess a number between 1 and 100 with the fewest guesses: "))

    if option == 0:
      break

    if option > guess_number:
        print("Too high. Try again.")
        count += 1
    else:
        print("Too low. Try again.")
        count += 1

    if count == 10:
        print( "Either you know the secret or you got lucky!" )

    elif count > 10:
        print( "You should be able to do better!")

    if option == guess_number:
        print("Congratulations. You guessed the number" + str(guess_number))
        break

  user_option = str(input("Would you like to play again? (y/n): "))
  if user_option == "n":
     break
  else:
     continue
