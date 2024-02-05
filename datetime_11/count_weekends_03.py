# write a program to count weekdays fri or sat . in specific month
from datetime import datetime
from dateutil.relativedelta import relativedelta
# inputs
year= 2023
month=6
given_date = datetime( year, month, 1)
end_date= given_date+relativedelta(months=1 ,day=1)
counter_weekends=0
while given_date<end_date:
    if given_date.date().weekday() in [4,5]: # monday =0 , fri=4 , sat=5
        counter_weekends +=1
    given_date=given_date+relativedelta(days=1)
print("count of weekends fri or sat=",counter_weekends)