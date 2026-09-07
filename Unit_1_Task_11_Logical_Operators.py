#and operators

a=5
result=a>2 and a<10
print("result of",a,">2and",a,"<10:",result)
a=1
result=a>2 and a<5
print("result of",a,">2and",a,"<5:",result)

# or operator

a=1
result=a>5 or a<10
print("result of",a,">5 or",a,"<10",result)
a=5
result=a<3 or a>8
print("result of",a,"<3 or",a,">8",result)

#not oprator
a=1
result=not(a>2 and a<10)
print("result of",result)
