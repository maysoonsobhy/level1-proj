# program to round a date to the nearest month start:[current or next]
#day >=15    :goto next month    1-1-2024
# day < 15    :goto current month 1-12-2023
from _datetime import datetime
from dateutil.relativedelta import relativedelta
given_date=datetime(2023,12,14) #result: 1-1-2024
if given_date.date().day>=15:
    given_date=given_date+relativedelta(months=1, day=1)
else:
    given_date=given_date+relativedelta(day=1)
print(given_date.date())




