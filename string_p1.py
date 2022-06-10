# Define check the given string is Palindrome String
str1 = input("Enter the String:")
str2 = str1[::-1]
if (str1 == str2):
    print("This string is Palindrome String")
else:
    print("This string is not Palindrome String")