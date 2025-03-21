sum = 0
average = 0
largest = 0
smallest = 99999999
product = 1

for number in range(3):
	number = int(input("Enter integers: "))
	sum += number
	product *= number

	if number > largest:
	   largest = number

	if number < smallest:
	   smallest = number

average = sum / 4



print('Sum Is: ', sum)
print('Average Is: ', average)
print('Product Is: ', product)
print('Largest Is: ', largest)
print('Smallest Is: ', smallest)


