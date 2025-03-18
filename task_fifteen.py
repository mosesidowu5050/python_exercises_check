num1 = float(input("Enter the first floating-point number: "))
num2 = float(input("Enter the second floating-point number: "))
num3 = float(input("Enter the third floating-point number: "))

if num1 <= num2 and num1 <= num3:
    if num2 <= num3:
        smallest, middle, largest = num1, num2, num3
    else:
        smallest, middle, largest = num1, num3, num2

elif num2 <= num1 and num2 <= num3:
    if num1 <= num3:
        smallest, middle, largest = num2, num1, num3
    else:
        smallest, middle, largest = num2, num3, num1

else: 
    if num1 <= num2:
        smallest, middle, largest = num3, num1, num2
    else:
        smallest, middle, largest = num3, num2, num1

print(smallest, middle, largest)
