
# Program to write a function calculate_average using handling exception
def average_number(num_list):
    try:
        return sum(num_list)/len(num_list)
    except TypeError as err_msg:
        print("Error:Non numeric value found in the list!",err_msg)
my_list=[10,20,"30z",40]
my_list=average_number(num_list=my_list)
print(my_list)