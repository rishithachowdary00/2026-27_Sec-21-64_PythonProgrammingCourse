N = int(input("Enter how many numbers: "))

number = int(input("Enter number 1: "))
largest = number

for i in range(2, N + 1):
    number = int(input(f"Enter number {i}: "))
    if number > largest:
        largest = number

print("The largest number is:", largest)
