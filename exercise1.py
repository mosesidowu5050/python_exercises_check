passes = 0
failures = 0

for student in range(10):
   number = int(input('Enter number (1=pass, 2=fail): '))

   while True:
    if number not in [1, 2]:
     number = int(input('Invalid, enter number (1=pass, 2=fail): '))
     continue

    else:
     break


   if number == 1:
      passes = passes + 1
   else:
      failures = failures + 1

print('Passes: ', passes)
print('Failures: ', failures)
