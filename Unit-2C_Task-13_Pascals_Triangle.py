# pascal_triangle 
n = int(input("Enter number of rows: "))
row = [1]

for i in range(n):
    print(" " * (n - i), *row)
    row = [1] + [row[j] + row[j+1] for j in range(len(row)-1)] + [1]