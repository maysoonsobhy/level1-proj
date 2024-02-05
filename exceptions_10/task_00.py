
# Program to write a function divide_num using handling exception
def divide_numbers(a,b):
    try:
        return a/b
    except ZeroDivisionError as err_msg:
        print("cannot divide by zero",err_msg)
print(divide_numbers(9,0))

