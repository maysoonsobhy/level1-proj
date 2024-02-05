import calendar
from datetime import datetime
from dateutil.relativedelta import relativedelta
import csv
contract_total_fees=600000
contract_deposit_fees=10000
year=2021
month=3
years=2024
start_date=datetime(year,month,day=1)
end_date=datetime(years,month,day=1)
dates_list=[]
while start_date < end_date :
    dates_list.append(start_date)
    start_date+=relativedelta(months=3)
sub=600000-10000
installment_amount=sub/12
max_grace_date=start_date+relativedelta(day=6,month=3,year=2021,weekday=calendar.SATURDAY)
if max_grace_date.day==6:
    max_grace_date=max_grace_date+relativedelta(days=1)
max_grace_date2=start_date+relativedelta(day=6,month=6,year=2021,weekday=calendar.SUNDAY)
max_grace_date3=start_date+relativedelta(day=6,month=9,year=2021,weekday=calendar.MONDAY)
max_grace_date4=start_date+relativedelta(day=6,month=12,year=2021,weekday=calendar.MONDAY)
max_grace_date5=start_date+relativedelta(days=6,month=3,year=2022,weekday=calendar.SUNDAY)
max_grace_date6=start_date+relativedelta(day=6,month=6,year=2022,weekday=calendar.MONDAY)
max_grace_date7=start_date+relativedelta(day=6,month=9,year=2022,weekday=calendar.TUESDAY)
max_grace_date8=start_date+relativedelta(day=6,month=12,year=2022,weekday=calendar.TUESDAY)
max_grace_date9=start_date+relativedelta(day=6,month=3,year=2023,weekday=calendar.MONDAY)
max_grace_date10=start_date+relativedelta(day=6,month=6,year=2023,weekday=calendar.TUESDAY)
max_grace_date11=start_date+relativedelta(day=6,month=9,year=2023,weekday=calendar.WEDNESDAY)
max_grace_date12=start_date+relativedelta(day=6,month=12,year=2023,weekday=calendar.WEDNESDAY)
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
      [10,dates_list[9],installment_amount,max_grace_date10],
      [11,dates_list[10],installment_amount,max_grace_date11],
      [12,dates_list[11],installment_amount,max_grace_date12])
with open("C:\\my_files\\102_El Ahly Bank.csv.csv","w",newline="") as my_file:
    writer=csv.writer(my_file)
    for row in list:
        writer.writerow(row)
