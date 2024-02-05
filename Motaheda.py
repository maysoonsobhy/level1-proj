import calendar
from datetime import datetime
from dateutil.relativedelta import relativedelta
import csv
start_date=datetime(day=1,month=1,year=2021)
installment_date=start_date+relativedelta(weekday=calendar.FRIDAY)
installment_date2=start_date+relativedelta(years=1,weekday=calendar.SATURDAY)
max_grace_date=start_date+relativedelta(day=8,month=1,year=2021,weekday=calendar.FRIDAY)
max_grace_date2=start_date+relativedelta(day=8,month=1,years=1,weekday=calendar.SATURDAY)
if max_grace_date.day ==8:
       max_grace_date=max_grace_date+relativedelta(days=2)
if max_grace_date2.day ==8:
       max_grace_date2=max_grace_date2+relativedelta(days=1)
installment_amount=500000/2
list=(["installment serial","installment date","installment amount","max grace date"],
[1,installment_date,installment_amount,max_grace_date],
[2,installment_date2,installment_amount,max_grace_date2])
input_file="C:\\my_files\\Contracts.csv"
output_file="C:\\my_files\\Company.csv"
with open(input_file,"r") as my_file, open(output_file,"w") as write_to_file:
    reader=csv.reader(my_file)
    writer=csv.writer(write_to_file)
    for row in list:
       writer.writerow(row)