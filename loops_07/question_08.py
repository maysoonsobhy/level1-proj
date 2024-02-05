company_employees = [(101, "Hayam Esam", 10000.0, "Engineer", "F"),
(102, "Ibrahim Ahmed", 9000.0, "Accountant", "M"),
(103, "Adham Aly", 5000.0, "Engineer","M"),
(104, "Islam Hassan", 7000.0, "Sales","M"),
(105, "Marwa Esam", 7000.0, "Marketer","F"),
(106, "Ola Hassan", 7000.0, "Engineer","F")]
count_M, count_F = 0, 0
for i in company_employees:
    if i[4] == 'M':
        count_M = count_M + 1
    elif i[4] == 'F':
        count_F = count_F + 1
print(count_M)
print(count_F)



