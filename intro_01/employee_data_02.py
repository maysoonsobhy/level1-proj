# write employee data
employee_id = 101                      # int data type
employee_name = "maysoon"              # string data type
employee_salary = 7000.0               # float data type
employee_job = " python Devoloper "       # string data type

print(".............string to string concat................")
print(employee_name + "works at" + employee_job)

print("...........string to int, float concatenation..........")
print("..........convert int, float to string [  casting  ].............")
print(employee_name + "has id =" + str(employee_id))
print(employee_name + " takes salary =" + str(employee_salary))


print("...........float to int casting...............")
invoice_total = 6000.55
invoice_total = int(invoice_total)
print(invoice_total)
print(type(invoice_total))




