number_one = int(input("Enter first number: "))
number_two = int(input("Enter second number: "))
number_three = int(input("Enter third number: "))


sum = number_one + number_two + number_three
average = sum / 3
product = number_one * number_two * number_three


print('Sum is: ', sum)
print(f"Average is: {average:.2f}")
print("Product is: " , product)


if number_one < number_two and number_one < number_three:
   smallest = number_one     
elif number_two < number_one and number_two < number_three:
   smallest = number_two
elif number_three < number_one and number_three < number_two:
   smallest = number_three

print('Smallest: ', smallest)
     

if number_one > number_two and number_one > number_three:
   largest = number_one     
elif number_two > number_one and number_two > number_three:
   largest = number_two
elif number_three > number_one and number_three > number_two:
   largest = number_three

print('Largest: ', largest)


