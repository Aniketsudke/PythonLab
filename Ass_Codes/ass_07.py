def condition1(x,y):
    print("%d is grater than %d"%(x,y))
    print("Square of %d is"%(x),x**2)
    print("Cude of %d is"%(y),y**3)
def condition2(x,y):
    print("%d is grater than %d"%(y,x))
    print("Square of %d is"%(y),y**2)
    print("Cude of %d is"%(x),x**3)
def condition3(x,y):
    print("%d is equals to %d"%(x,y))
    print("Square root of %d and %d is"%(x,y),x**(1/2))
    print("Cude root of %d and %d is"%(x,y),y**(1/3))

a = int(input("Enter the value :"))
b = int(input("Enter the another value :"))
if a>b:
    condition1(a,b)
elif a<b:
    condition2(a,b)
else:
    condition3(a,b)
