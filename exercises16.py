for number1 in range(1, 21):
    for number2 in range(number1, 21): 
        for number3 in range(number2, 21):
            if number1 **2 + number2 **2 == number3 **2:
                print(f"({number1}, {number2}, {number3})")
