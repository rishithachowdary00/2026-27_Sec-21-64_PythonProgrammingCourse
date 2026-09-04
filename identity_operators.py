# identity_operators
# is
a=[1,2,3]
b=[1,2,3]
c = a is b
print("result of c is :",c)
a=[3,4,5]
b=a
c= a is b
print("result of c is :",c)

# is not
a=[2]
b=[2]
c= a is not b
print( "result of c is :",c)

a=[2]
b=a
c= a is not b
print("result of c is :",c)