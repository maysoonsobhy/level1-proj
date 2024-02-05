

# write a program to count weekday fri in a specific month
import calendar
from datetime import datetime
from dateutil.relativedelta import relativedelta
year=2023
month=9
input_date=datetime(year,month,1)
count = 0
for i in range(month):
   if input_date.month == month:
    input_date=input_date+relativedelta(weekday=calendar.FRIDAY,weeks=1)
    count += 1
print("Count of weekend days =",count)

