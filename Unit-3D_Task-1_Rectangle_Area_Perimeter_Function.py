l= float(input("enter length:"))
b= float(input("enter breadth:"))
def rectangle(l,b):
    area=l*b
    perimeter=2*(l+b)
    return area,perimeter
area,perimeter=rectangle(l,b)
print("area of rectangle is ",area)
print("perimeter of rectangle is",perimeter)