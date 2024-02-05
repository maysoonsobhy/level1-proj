
# Write a python program to capitalize the first and last letters of each word in a given string
str1 = "python exercises practice solution"
for i in str1.split():
    print(i[0].upper() +i[1:-1] +i[-1].upper(),end=' ')
