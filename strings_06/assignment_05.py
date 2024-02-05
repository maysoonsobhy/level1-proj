

# Write a program that takes an input string and displays its letters in alphabetical order.
str = input("Enter the String: ")
str = sorted(str)
str = ''.join(str)
print("The sorted String is:", str)
