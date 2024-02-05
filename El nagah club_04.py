import calendar
from datetime import datetime
from dateutil.relativedelta import relativedelta
import csv
start_date=datetime(day=1,month=3,year=2021)
end_date=datetime(day=1,month=3,year=2024)
dates_list=[]
while start_date < end_date:
    dates_list.append(start_date)
    start_date+=relativedelta(months=1)
installment_amount=700000/36
max_grace_date=start_date+relativedelta(day=4,month=3,year=2021,weekday=calendar.THURSDAY)
max_grace_date2=start_date+relativedelta(day=4,month=4,year=2021,weekday=calendar.SUNDAY)
max_grace_date3=start_date+relativedelta(day=4,month=5,year=2021,weekday=calendar.TUESDAY)
max_grace_date4=start_date+relativedelta(day=4,month=6,year=2021,weekday=calendar.FRIDAY)
if max_grace_date4.day==4:
    max_grace_date4=max_grace_date4+relativedelta(days=2)
max_grace_date5=start_date+relativedelta(day=4,month=7,year=2021,weekday=calendar.SUNDAY)
max_grace_date6=start_date+relativedelta(day=4,month=8,year=2021,weekday=calendar.WEDNESDAY)
max_grace_date7=start_date+relativedelta(day=4,month=9,year=2021,weekday=calendar.SATURDAY)
if max_grace_date7.day==4:
    max_grace_date7=max_grace_date7+relativedelta(days=1)
max_grace_date8=start_date+relativedelta(day=4,month=10,year=2021,weekday=calendar.MONDAY)
max_grace_date9=start_date+relativedelta(day=4,month=11,year=2021,weekday=calendar.THURSDAY)
max_grace_date10=start_date+relativedelta(day=4,month=12,year=2021,weekday=calendar.SATURDAY)
if max_grace_date10.day==4:
    max_grace_date10=max_grace_date10+relativedelta(days=1)
max_grace_date11=start_date+relativedelta(day=4,month=1,year=2022,weekday=calendar.TUESDAY)
max_grace_date12=start_date+relativedelta(day=4,month=2,year=2022,weekday=calendar.FRIDAY)
if max_grace_date12.day==4:
    max_grace_date12=max_grace_date12+relativedelta(days=2)
max_grace_date13=start_date+relativedelta(day=4,month=3,year=2022,weekday=calendar.FRIDAY)
if max_grace_date13.day==4:
    max_grace_date13=max_grace_date13+relativedelta(days=2)
max_grace_date14=start_date+relativedelta(day=4,month=4,year=2022,weekday=calendar.MONDAY)
max_grace_date15=start_date+relativedelta(day=4,month=5,year=2022,weekday=calendar.WEDNESDAY)
max_grace_date16=start_date+relativedelta(day=4,month=6,year=2022,weekday=calendar.SATURDAY)
if max_grace_date16.day==4:
    max_grace_date16=max_grace_date16+relativedelta(days=1)
max_grace_date17=start_date+relativedelta(day=4,month=7,year=2022,weekday=calendar.MONDAY)
max_grace_date18=start_date+relativedelta(day=4,month=8,year=2022,weekday=calendar.THURSDAY)
max_grace_date19=start_date+relativedelta(day=4,month=9,year=2022,weekday=calendar.SUNDAY)
max_grace_date20=start_date+relativedelta(day=4,month=10,year=2022,weekday=calendar.TUESDAY)
max_grace_date21=start_date+relativedelta(day=4,month=11,year=2022,weekday=calendar.FRIDAY)
if max_grace_date21.day==4:
    max_grace_date21=max_grace_date21+relativedelta(days=2)
max_grace_date22=start_date+relativedelta(day=4,month=12,year=2022,weekday=calendar.SUNDAY)
max_grace_date23=start_date+relativedelta(day=4,month=1,year=2023,weekday=calendar.WEDNESDAY)
max_grace_date24=start_date+relativedelta(day=4,month=2,year=2023,weekday=calendar.SATURDAY)
if max_grace_date24.day==4:
    max_grace_date24=max_grace_date24+relativedelta(days=1)
max_grace_date25=start_date+relativedelta(day=4,month=3,year=2023,weekday=calendar.SATURDAY)
if max_grace_date25.day==4:
    max_grace_date25=max_grace_date25+relativedelta(days=1)
max_grace_date26=start_date+relativedelta(day=4,month=4,year=2023,weekday=calendar.TUESDAY)
max_grace_date27=start_date+relativedelta(day=4,month=5,year=2023,weekday=calendar.THURSDAY)
max_grace_date28=start_date+relativedelta(day=4,month=6,year=2023,weekday=calendar.SUNDAY)
max_grace_date29=start_date+relativedelta(day=4,month=7,year=2023,weekday=calendar.TUESDAY)
max_grace_date30=start_date+relativedelta(day=4,month=8,year=2023,weekday=calendar.FRIDAY)
if max_grace_date30.day==4:
    max_grace_date30=max_grace_date30+relativedelta(days=2)
max_grace_date31=start_date+relativedelta(day=4,month=9,year=2023,weekday=calendar.MONDAY)
max_grace_date32=start_date+relativedelta(day=4,month=10,year=2023,weekday=calendar.WEDNESDAY)
max_grace_date33=start_date+relativedelta(day=4,month=11,year=2023,weekday=calendar.SATURDAY)
if max_grace_date33.day==4:
    max_grace_date33=max_grace_date33+relativedelta(days=1)
max_grace_date34=start_date+relativedelta(day=4,month=12,year=2023,weekday=calendar. MONDAY)
max_grace_date35=start_date+relativedelta(day=4,month=1,year=2024,weekday=calendar.THURSDAY)
max_grace_date36=start_date+relativedelta(day=4,month=2,year=2024,weekday=calendar.SUNDAY)
list=(["installment serial","installment date","installment_amount","max grace date"],
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
      [12,dates_list[11],installment_amount,max_grace_date12],
      [13,dates_list[12],installment_amount,max_grace_date13],
      [14,dates_list[13],installment_amount,max_grace_date14],
      [15,dates_list[14],installment_amount,max_grace_date15],
      [16,dates_list[15],installment_amount,max_grace_date16],
      [17,dates_list[16],installment_amount,max_grace_date17],
      [18,dates_list[17],installment_amount,max_grace_date18],
      [19,dates_list[18],installment_amount,max_grace_date19],
      [20,dates_list[19],installment_amount,max_grace_date20],
      [21,dates_list[20],installment_amount,max_grace_date21],
      [22,dates_list[21],installment_amount,max_grace_date22],
      [23,dates_list[22],installment_amount,max_grace_date23],
      [24,dates_list[23],installment_amount,max_grace_date24],
      [25,dates_list[24],installment_amount,max_grace_date25],
      [26,dates_list[25],installment_amount,max_grace_date26],
      [27,dates_list[26],installment_amount,max_grace_date27],
      [28,dates_list[27],installment_amount,max_grace_date28],
      [29,dates_list[28],installment_amount,max_grace_date29],
      [30,dates_list[29],installment_amount,max_grace_date30],
      [31,dates_list[30],installment_amount,max_grace_date31],
      [32,dates_list[31],installment_amount,max_grace_date32],
      [33,dates_list[32],installment_amount,max_grace_date33],
      [34,dates_list[33],installment_amount,max_grace_date34],
      [35,dates_list[34],installment_amount,max_grace_date35],
      [36,dates_list[35],installment_amount,max_grace_date36])
with open("C:\\my_files\\104-El Nagah Club.csv.csv","w",newline="") as my_file:
    writer = csv.writer(my_file)
    for row in list:
        writer.writerow(row)