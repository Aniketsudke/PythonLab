def binarysearch(list1,element):
    start=0
    end=len(list1)-1
    mid=0
    while start<=end:
        mid=(end+start)//2
        if list1[mid]<element:
            start=mid+1
        elif list1[mid]>element:
            end=mid-1
        else:
            return mid
    return -1
list1=[1,2,3,4,5,6,7,8,9,10,15,16,17,18,19]
print("list is",list1)
n=int(input("Enter the number:"))
element_search=n
my_result=binarysearch(list1,element_search)
if my_result !=1:
    print("Element found at index",str(my_result))
else:
    print("Element not found")