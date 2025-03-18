age = int(input("Enter your age: "))

maximum_heart_rate = 220 - age

target_minimum = maximum_heart_rate * 0.50
target_maximum = maximum_heart_rate * 0.85

print("\nMaximum Heart Rate is: ", maximum_heart_rate, "beats per minute")

print("Heart Rate Range is: ", target_minimum, "-", target_maximum, "beats per minute")
