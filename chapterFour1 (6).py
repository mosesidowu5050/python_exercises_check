import random


def learn_addition(number_one, number_two):
    return number_one + number_two


def learn_subtractions(number_one, number_two):
    return number_one - number_two


def learn_multiplications(number_one, number_two):
    return number_one * number_two


def learn_divisions(number_one, number_two):
    return number_one / number_two


counter = 1
count = 1

levels = int(input("Enter level from (1 to 4): "))
if levels == 1:

    while True:
        number_one = random.randint(10, 100)
        number_two = random.randint(10, 100)

        print(f"How much is ", number_one, "+", number_two, "?\n")
        print("press 00 to quit")
        answer = int(input("What's your answer? : "))

        if answer == 00:
            break

        result = learn_addition(number_one, number_two)
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
        first_num = random.randint(10, 30)
        second_num = random.randint(10, 30)

        print(f"How much is ", first_num, "-", second_num, "?\n")
        print("press 00 to quit")
        answer = int(input("What's your answer? : "))

        if answer == 00:
            break

        result = learn_subtractions(first_num, second_num)
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

if levels == 3:
    while True:
        value_one = random.randint(10, 30)
        value_two = random.randint(10, 30)

        print(f"How much is ", value_one, "times", value_one, "?\n")
        print("press 00 to quit")
        answer = int(input("What's your answer? : "))

        if answer == 00:
            break

        result = learn_multiplications(value_one, value_one)
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

if levels == 4:
    while True:
        first_number = random.randint(10, 100)
        second_number = random.randint(10, 100)

        print(f"How much is ", first_number, "/", second_number, "?\n")
        print("press 00 to quit")
        user_answer = float(input("What's your answer? : "))
        answer = round(user_answer, 2)

        if answer == 00:
            break

        user_result = learn_divisions(first_number, second_number)
        result = round(user_result, 2)
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
