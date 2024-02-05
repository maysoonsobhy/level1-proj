
# Program to write a function perform_ope using handling exception
def perform_operation(a, b , operation):
    try:
        if operation =="+":
            return a+b
        elif operation =="-":
            return a-b
        elif operation =="*":
            return a*b
        elif operation=="/":
            return a/b
    except ZeroDivisionError as err_msg:
        print("Division by zero is not allowed!",err_msg)
print(perform_operation(10,0,"/"))