# here we will show strings function with examples
print("........Great and printing strings......")
emp_name = "maysoon"
print(emp_name)
print(type(emp_name))

print(".....upper() , lower strings functions.........")
upper_emp_name = emp_name.upper()
lower_emp_name = emp_name.lower()
print(upper_emp_name)
print(lower_emp_name)

print("..............endswith(),string function........")
file_path = "c:/my_Documents/egypt.pdf"
file_path = file_path.lower()
if file_path.endswith("pdf"):
    print("it is book")
elif file_path.endswith("jpg") or file_path.endswith("png"):
     print("it is image")
else:
    print("unknown file type")



print("........isupper(),islower,isalpha strings functions...........")
print(upper_emp_name.isupper())
print(lower_emp_name.islower())
print(upper_emp_name.isalpha())