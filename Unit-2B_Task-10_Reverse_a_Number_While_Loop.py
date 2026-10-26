number = int(input("Enter a number: "))

n = abs(number)   # handle negative numbers
reverse = 0

while n > 0:
    digit = n % 10
    reverse = reverse * 10 + digit
    n //= 10

if number < 0:
    reverse = -reverse

print("Reversed number:", reverse)
