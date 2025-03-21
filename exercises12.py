miles_per_gallon = 0
total_miles_per_gallon = 0
overall_average = 0
count = 0

while True:
   gallons_used = float(input("Enter the gallons used (-1 to end): "))
   if gallons_used == -1:
     break

   miles_driven = int(input("Enter the miles driven: "))
   miles_per_gallon =  miles_driven / gallons_used
   count += 1
   total_miles_per_gallon += miles_per_gallon
   print(f'The miles/gallon for this tank was: {miles_per_gallon}')

   overall_average = total_miles_per_gallon / count
print(f'The overall average miles/gallon was: {overall_average:.6f}')
