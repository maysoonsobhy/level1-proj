# Program to get a max number
def max_number(list):
    max = 0
    for item in list:
        if item > max:
            max = item
    return max
# Main program
my_list = [88,15,33,255,20,1]
max_num = max_number(list=my_list)
print(max_num,(type(max_num)))