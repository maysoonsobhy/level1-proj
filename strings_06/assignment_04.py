
# Develop a program that checks whether a given string is a palindrome or not.
str = input("Enter a string : ")
if(str == str[:: - 1]):
   print("This is a Palindrome.")
else:
   print(" This not a palindrome.")

