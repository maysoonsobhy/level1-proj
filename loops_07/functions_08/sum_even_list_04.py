# function to return sum of even numbers from list
import math


def sum_even_list(my_list):
    sum_even = 0
    for item in my_list:
        if item % 2==0:
            sum_even = sum_even + item
    return sum_even
# main program
test_list = [15,6,22,20,30,7,9]
s_even = sum_even_list(my_list = test_list)
print("sum of even num =" , s_even )

print(math.pow(2,3)) # positional
print(s_even , end= "")  # keyword argument
test_list.sort(reverse = True) # keyword argument