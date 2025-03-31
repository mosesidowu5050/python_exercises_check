def average(numbers, *args):
    return (numbers + sum(args)) / (1 + len(args))


result = average(5)
print(result)
