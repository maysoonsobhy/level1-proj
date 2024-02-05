

# Write a program to remove duplicated words and leave unique words in a string and ignore case sensitive
str = "Hello world world Python is great great Python"
print(' '.join(dict.fromkeys(str.split())))
