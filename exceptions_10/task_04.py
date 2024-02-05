
# Write a program that takes integer from user and calculate square root using handling exception
import math
try:
    num=int(input("Enter the number:"))
    result=math.sqrt(num)
    print(num)
except ValueError as err_msg:
    print("Math domain error",",",err_msg)

