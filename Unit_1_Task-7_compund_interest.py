principal = float(input("Enter Principal Amount: "))
rate = float(input("Enter Annual Interest Rate : "))
time = float(input("Enter the time : "))
amount = principal * (1 + (rate / 100) **(time))
compound  = amount - principal
print("COMPOUND INTEREST",compound )