import random

def learn_multiplication(number_one, number_two):
    return number_one * number_two


counter = 1
count = 1

levels = int(input("Enter level press 1 (for single-digit) and 2 (for large-digit): "))
if levels == 1:

  while True:
    number_one = random.randint(1, 9)
    number_two = random.randint(1, 9)

    print(f"How much is ", number_one, "times", number_two, "?\n")
    print("press 0 to quit")
    answer = int(input("What's your answer? : "))


    if answer == 0:
        break

    result = learn_multiplication(number_one, number_two)
    if answer == result and count == 1:
        count += 1
        print("Very Good!")


    elif answer == result and count == 2:
        count += 1
        print("Nice work!")
    elif answer == result and count == 3:
        print("Keep up the good work!")

    if answer != result and counter == 1:
        print("No. Please try again.")
        counter += 1

    elif answer != result and counter == 2:
        counter += 1
        print("Wrong. Try once more.")

    elif answer != result and counter == 3:
        print("No. Keep trying.")
        continue


if levels == 2:
    while True:
        value_one = random.randint(10, 30)
        value_two = random.randint(10, 30)

        print(f"How much is ", value_one, "times", value_one, "?\n")
        print("press 0 to quit")
        answer = int(input("What's your answer? : "))

        if answer == 0:
            break

        result = learn_multiplication(value_one, value_one)
        if answer == result and count == 1:
            count += 1
            print("Very Good!")


        elif answer == result and count == 2:
            count += 1
            print("Nice work!")
        elif answer == result and count == 3:
            print("Keep up the good work!")

        if answer != result and counter == 1:
            print("No. Please try again.")
            counter += 1

        elif answer != result and counter == 2:
            counter += 1
            print("Wrong. Try once more.")

        elif answer != result and counter == 3:
            print("No. Keep trying.")
            continue

