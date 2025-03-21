for star in range(10):
   for asterisks in range(star + 1):
     print('*', end= '')
   print()


print()


for star in range(10, 0, -1):
    for asterisks in range(star):
        print('*', end='')
    print()


print()


for star in range(1, 10):  
    for asterisks in range(1, star):
        print(" ", end="")
    
    for looping in range(star, 10):
        print("*", end="")
    print()  


print()


for star in range(1, 10):
    for asterisks in range(star, 10): 
       print(" ", end="")
    for looping in range(1, star):
        print("*", end="")
    print()


