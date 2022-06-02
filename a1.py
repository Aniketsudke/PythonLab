a = int(input("Enter the first number:"))
b = int(input("Enter the second number:"))
c = int(input("Enter the third number:"))

if a > b:
    if a > c:
        print(a,"is grater than ",b, "and",c)

elif b > a:
    if b > c:
        print(b,"is grater than ",a, "and",c)

elif c > a:
    if c > b:
        print(c,"is grater than ",b, "and",a)