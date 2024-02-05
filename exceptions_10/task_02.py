# Write a program that reads integer value from user using handling exception
while(True):
    try:
        x=int(input("enter the number:"))
        break
    except ValueError as err_msg:
        print("Input integer only",err_msg)