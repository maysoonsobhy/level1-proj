# program to calculate monthly net salary based on monthly gross salary
# tax = 10%   G.S  >=5000

emp_name = "maysoon"
emp_gross_salary  = 7000.0

if emp_gross_salary>=500:
    tax =10
else:
    tax = 0
monthly_net_salary = emp_gross_salary - emp_gross_salary * tax /100
print("monthly net =  ")