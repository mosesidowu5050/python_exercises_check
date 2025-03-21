number = int(input("Enter a five digit integer: "))

divisor = 10000  

while divisor > 0:

    digit = number // divisor  
    print(digit, end="   ")  
    number %= divisor
    divisor //= 10  

print() 
