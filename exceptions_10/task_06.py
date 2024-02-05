
# Program to write a function fetch_element using handling exception
def fetch_element(dict,key):
    try:
        value=my_dict["c"]
        print(value)
    except KeyError as err_msg:
        print("Key 'c' not found in the dict! ",err_msg)
my_dict={"a":1,"b":2}
my_dict=fetch_element(dict,key=my_dict)
print(my_dict)