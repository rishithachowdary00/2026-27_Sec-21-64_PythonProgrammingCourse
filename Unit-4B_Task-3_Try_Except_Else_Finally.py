# Example solution: try-except-else-finally (square of an integer)
try:
    text = input("Enter a number: ")
    number = int(text)
except ValueError:
    print("That is not a valid integer.")
else:
    print("Square:", number * number)
finally:
    print("Program finished.")