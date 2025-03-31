def arbitrary_function(result=None, *numbers):
    for number in numbers:
        result *= number
    return result


print(arbitrary_function(2, 3, 4))

