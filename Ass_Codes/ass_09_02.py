list1 = [1,5,6,7,2,84,46,63,26,265,235,565,64,635,56]
print(list1)
num = int(input("Enter the value :"))
for i in range(len(list1)):
    if (num == list1[i]):
         y = list1.index(num)
print("Index of number :",y)