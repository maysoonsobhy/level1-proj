

# Count occurrences of a specific date in list:
from datetime import datetime
dates_list=[datetime(2023,12,31),datetime(2023,8,15),
            datetime(2023,8,15),datetime(2023,5,1)]
given_date=datetime(2023,8,15)
count=0
for i in dates_list:
    if i == given_date:
        count=count+1
print(given_date,"occurs",count)