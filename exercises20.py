approximating = 1

for number in range(1, 10):
    factorial = 1  

    for check in range(1, number + 1):
        factorial *= number
    
    approximating += 1 / factorial

print(f"Approximated value of e: {approximating:.3f}")
