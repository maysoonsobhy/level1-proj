

# Create a list of dates within a date range:
import calendar
from datetime import datetime
from dateutil.relativedelta import relativedelta
start_range=datetime(2023,1,1)
end_range=datetime(2023,1,10)
dates_list=[]
while start_range <= end_range:
    dates_list.append(start_range)
    start_range += relativedelta(days=1)
print(dates_list)