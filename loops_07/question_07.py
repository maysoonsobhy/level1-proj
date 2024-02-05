str = input("enter str")
word = input("enter word")
count = 0
for i in range(len(str)):
    if str[i:i+len(word)] == word:
        count += 1
print(count)