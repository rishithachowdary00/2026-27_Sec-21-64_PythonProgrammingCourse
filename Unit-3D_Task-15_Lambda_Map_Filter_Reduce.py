from functools import reduce

numbers = [1, 2, 3, 4, 5]

# map() - Square each number
squares = list(map(lambda x: x*x, numbers))
print("Squares:", squares)

# filter() - Select even numbers
even = list(filter(lambda x: x % 2 == 0, numbers))
print("Even numbers:", even)

# reduce() - Find sum of all numbers
total = reduce(lambda x, y: x + y, numbers)
print("Sum:", total)