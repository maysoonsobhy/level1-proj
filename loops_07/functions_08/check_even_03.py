# Ex No. 3: # creat a function to check a number if it is even number:
# function : check_even function , parameter:1 parameter[int],
"""""
def even_number(num):
#if (num%2==0):
#   return True
#else:
#return False
    is_even = False # flag method2
    if num%2==0:
        is_even = True
    return is_even
    #return num %2==0 # method3
# main program
result = even_number(12)
#print(result)
if result:
    print("it is even num")
else:
    print("it is odd num")
"""""
def even_num(n):
    my_dict={}
    if n %2==0:
        my_dict[n] = True
    else:
        my_dict[n] = False
    return my_dict
res_dict = even_num(3)
print(res_dict)

