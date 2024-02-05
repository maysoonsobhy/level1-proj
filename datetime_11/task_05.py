

# Check if all dates in a list are in the same month:
from datetime import datetime
from dateutil.relativedelta import relativedelta
dates_list=[datetime(2023,12,31),datetime(2023,12,15),
            datetime(2023,12,15),datetime(2023,12,1)]
for i in dates_list:
    if i ==dates_list[0]:
        print("All dates are in the same month:",datetime.now().date().month)