number = int(input("Enter a number: "))

n = abs(number)   # handle negative numbers
sum_of_digits = 0

while n > 0:
    digit = n % 10
    sum_of_digits += digit
    n //= 10

print("Sum of digits:", sum_of_digits)
