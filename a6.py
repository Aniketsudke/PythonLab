
for i in range(100,1000,1):
    n = i
    sum = 0
    while n>0 :
        digit = n%10
        n = n//10
        sum = sum + digit**3
    if i == sum :
        print(i,end=" ")
