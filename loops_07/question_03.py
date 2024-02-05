def check_element(my_list,num):
    if num in my_list:
        return my_list.index(num)
    else:
        return None
#Main Program
lst = [6,8,4,9]
n=6
index=check_element(lst,n)
print(index)