import calendar
from datetime import datetime
from dateutil.relativedelta import relativedelta
import csv
start_date=datetime(day=1,month=1,year=2021)
end_date=datetime(day=1,month=1,year=2026)
dates_list=[]
while start_date < end_date:
    dates_list.append(start_date)
    start_date+=relativedelta(months=6)
sub=1000000-200000
installment_amount=sub/10
max_grace_date=start_date+relativedelta(day=11,month=1,year=2021,weekday=calendar.MONDAY)
max_grace_date2=start_date+relativedelta(day=11,month=7,year=2021,weekday=calendar.SUNDAY)
max_grace_date3=start_date+relativedelta(day=11,month=1,year=2022,weekday=calendar.TUESDAY)
max_grace_date4=start_date+relativedelta(day=11,month=7,year=2022,weekday=calendar.MONDAY)
max_grace_date5=start_date+relativedelta(day=11,month=1,year=2023,weekday=calendar.WEDNESDAY)
max_grace_date6=start_date+relativedelta(day=11,month=7,year=2023,weekday=calendar.TUESDAY)
max_grace_date7=start_date+relativedelta(day=11,month=1,year=2024,weekday=calendar.THURSDAY)
max_grace_date8=start_date+relativedelta(day=11,month=7,year=2024,weekday=calendar.THURSDAY)
max_grace_date9=start_date+relativedelta(day=11,month=1,year=2025,weekday=calendar.SATURDAY)
if max_grace_date9.day==11:
    max_grace_date9=max_grace_date9+relativedelta(days=1)
max_grace_date10=start_date+relativedelta(day=11,month=7,year=2025,weekday=calendar.FRIDAY)
if max_grace_date10.day==11:
    max_grace_date10=max_grace_date10+relativedelta(days=2)
list=(["installment serial","installment date","installment amount","max grace date"],
      [1,dates_list[0],installment_amount,max_grace_date],
      [2,dates_list[1],installment_amount,max_grace_date2],
      [3,dates_list[2],installment_amount,max_grace_date3],
      [4,dates_list[3],installment_amount,max_grace_date4],
      [5,dates_list[4],installment_amount,max_grace_date5],
      [6,dates_list[5],installment_amount,max_grace_date6],
      [7,dates_list[6],installment_amount,max_grace_date7],
      [8,dates_list[7],installment_amount,max_grace_date8],
      [9,dates_list[8],installment_amount,max_grace_date9],
      [10,dates_list[9],installment_amount,max_grace_date10])
with open("C:\\my_files\\106-Masters Edu.csv.csv","w",newline="") as my_file:
    writer=csv.writer(my_file)
    for row in list:
        writer.writerow(row)