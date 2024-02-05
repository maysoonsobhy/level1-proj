# program to construct the following pattern
num = 9
for i in range(num+1):
    for x in range(i):
        print(i,end="")
    print("")

for i in range(1,10):
    x= str(i)
    print(x*i)