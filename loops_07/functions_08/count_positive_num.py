# Program to count positive numbers
def count_positive_num(list):
    count = 0
    for item in list:
        if item >0:
            count+=1
    return count
# Main program
my_lst = [6,-7,1,-4,2,-3,8]
count_pos = count_positive_num(list=my_lst)
print(count_pos,(type(count_pos)))