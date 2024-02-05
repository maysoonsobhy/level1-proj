
# Count occurrences of a word in string
str = "A computer science portal for portal"
word ="portal"
words = str.split()
count = 0
for i in words:
   if i == word:
      count += 1
print(count)