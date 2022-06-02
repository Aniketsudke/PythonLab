'''
    *
   * *
  * * *
 * * * *
* * * * *
 * * * *
  * * *
   * *
    *
'''
n = 5
for i in range(5):
    for space in range(1,5-i):
        print(end=" ")
    for star in range(i+1):
        print("*",end=" ")
    print()
for i in range(4):
    for space in range(0,i+1):
        print(end=" ")
    for star in range(0,4-i):
        print("*",end=" ")
    print()
