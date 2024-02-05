

# Find the earliest date from a list
from datetime import datetime
dates_list=[datetime(2023,12,31),
            datetime(2023,8,15),
            datetime(2023,5,1)]
oldest=min(dates_list)
print(oldest)