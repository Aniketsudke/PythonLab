num = int(input("Enter a Number:"))
n = num
sum = 0
while n>0 :
    digit = n%10
    n = n//10
    sum = sum + digit**3
if num == sum :
    print(num,"is Armstrong")
else :
    print(num,"is not Armstrong")