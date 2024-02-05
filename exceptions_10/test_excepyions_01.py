# program to show exceptions type and how to solve
try:
    first_number= int(input("enter first number : " ) )
    seccond_number=int(input("enter second number:"))

    res=first_number/seccond_number
    print(res)
    open("c:\\my_files\\programming.txt")

except ValueError as err_msg:
    print("please enter only numbers not text",err_msg)
except ZeroDivisionError as err_msg:
    print("cannot divide by zero !!",err_msg)
except Exception as err_msg:
    print("Error happend _please contact admin 0107765645",err_msg)
finally:
    print("this is finally statement _ execute any time")
print("continue ")