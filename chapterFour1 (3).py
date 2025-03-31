import random


def learn_multiplication(number_one, number_two):
    return number_one * number_two



while True:
    number_one = random.randint(1, 20)
    number_two = random.randint(1, 20)

    print(f"How much is ", number_one, "times", number_two, "?\n")
    answer = int(input("What's your answer: "))

    result = learn_multiplication(number_one, number_two)
    if answer == result:
        print("Very Good!")
        break
    else:
        print("No. Please try again.")
        continue
