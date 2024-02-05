
# Program to write a function extract_element using handling exception
list=[1,2,3]
def extract_element(lst,index):
    try:
        print(lst[5])
    except IndexError as err_msg:
        print("Index out of range!",err_msg)
print(extract_element(lst=list,index=5))