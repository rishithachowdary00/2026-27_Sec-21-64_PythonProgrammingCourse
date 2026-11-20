balance = 1000

def deposit(amount):
    global balance
    balance += amount
    print("Balance after deposit:", balance)

def local_balance(amount):
    balance = amount
    print("Local balance:", balance)

print("Initial balance:", balance)
deposit(500)
local_balance(200)
print("Final bank balance:", balance)