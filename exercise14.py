first_largest = 0
second_largest = 0

for number in range(10):  
    numbers = int(input(f"Enter number {number+1}: "))

    if numbers > first_largest:
        second_largest = first_largest  
        first_largest = numbers  
    elif numbers > second_largest and numbers != first_largest:
        second_largest = numbers 


print(f"The first largest number is: {first_largest}")
print(f"The second largest number is: {second_largest}")



