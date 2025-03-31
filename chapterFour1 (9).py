#F = (9 / 5) * C + 32

def fahrenheit_to_celsius(fahrenheit):
    celsius = (fahrenheit - 32) * 5/9
    return celsius


celsius = 100
result = fahrenheit_to_celsius(celsius)
print(round(result, 2))
