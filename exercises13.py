numbers = int(input("Enter the number: "))

factorial = 1 
for number in range(1, numbers + 1):
    factorial *= number
    print(factorial)
print(f"Factorial is: {factorial}")
