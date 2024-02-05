# Program to search array number
def array_number(list,num):
    for i in range(len(list)):
        if list[i]== num:
            return list[i]
    return-1
# Main program
my_lst = [5,2,9,4]
print(array_number(my_lst,9))



