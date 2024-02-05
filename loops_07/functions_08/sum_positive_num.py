# Program to sum positive numbers
def sum_positive_num(list):
    sum_pos = 0
    for item in list:
        if item >0:
            sum_pos = sum_pos + item
    return sum_pos
# Main program
my_lst = [1,-5,7,-3,-8,9]
sum_positive = sum_positive_num(list=my_lst)
print(sum_positive , (type(sum_positive)))
