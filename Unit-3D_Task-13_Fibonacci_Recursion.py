def fibonacci(a):
    if a <= 1:
        return a
    return fibonacci(a - 1) + fibonacci(a - 2)
a= int(input("Enter number of terms: "))

for i in range(a):
    print(fibonacci(i), end=" ")