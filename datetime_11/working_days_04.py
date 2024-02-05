# program to get the date after 12 working days from a date
from datetime import datetime
from dateutil.relativedelta import relativedelta
given_date = datetime.now() # result = 11-1-2024
jump_days=12
for i in range (jump_days):
    if given_date.date().weekday() == 3: # if today is thursday
        given_date=given_date+relativedelta(days=3)
    elif given_date.date().weekday() ==4: # if today is friday
        given_date=given_date+relativedelta(days=2)
    else:
        given_date=given_date+relativedelta(days=1)
print(given_date)