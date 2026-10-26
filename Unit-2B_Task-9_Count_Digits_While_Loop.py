number = int(input("Enter a number: "))

n = abs(number)   # handle negative numbers
count = 0

while n > 0:
    count += 1
    n //= 10

print("Number of digits:", count)
