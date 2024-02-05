import calendar
from datetime import datetime
from dateutil.relativedelta import relativedelta
import csv
start_date=datetime(day=1,month=4,year=2021)
end_date=datetime(day=1,month=4,year=2026)
dates_list=[]
while start_date < end_date:
    dates_list.append(start_date)
    start_date+=relativedelta(years=1)
sub=900000-300000
installment_amount=sub/5
max_grace_date=start_date+relativedelta(day=15,month=4,year=2021,weekday=calendar.THURSDAY)
max_grace_date2=start_date+relativedelta(day=15,month=4,year=2022,weekday=calendar.FRIDAY)
if max_grace_date2.day==15:
    max_grace_date2=max_grace_date2+relativedelta(days=2)
max_grace_date3=start_date+relativedelta(day=15,month=4,year=2023,weekday=calendar.SATURDAY)
if max_grace_date3.day==15:
    max_grace_date3=max_grace_date3+relativedelta(days=1)
max_grace_date4=start_date+relativedelta(day=15,month=4,year=2024,weekday=calendar.MONDAY)
max_grace_date5=start_date+relativedelta(day=15,month=4,year=2025,weekday=calendar.TUESDAY)
list=(["installment serial","installment date","installment amount","max grace date"],
      [1,dates_list[0],installment_amount,max_grace_date],
      [2,dates_list[1],installment_amount,max_grace_date2],
      [3,dates_list[2],installment_amount,max_grace_date3],
      [4,dates_list[3],installment_amount,max_grace_date4],
      [5,dates_list[4],installment_amount,max_grace_date5],)
with open("C:\\my_files\\105-CSR CO.csv.csv","w",newline="") as my_file:
    writer=csv.writer(my_file)
    for row in list:
        writer.writerow(row)