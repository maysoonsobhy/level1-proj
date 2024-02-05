# Program to get minimum number
def minimum_number(list):
    min =list[0]
    for item in list:
        if item < min:
            min = item
    return min
# Main program
my_list = [77,15,300,90,22,60]
min_num = minimum_number(list = my_list)
print(min_num,(type(min_num)))