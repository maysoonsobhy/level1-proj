import random

first_num =random.randint(1,100)
second_num = random.randint(1,100)
print(str(first_num)+"+"+str(second_num))
res=int(input())
if res == first_num+second_num:
    print("correct ")
else:
    print("wrong")

