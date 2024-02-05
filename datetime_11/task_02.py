
# Check the specific date
from datetime import datetime
given_date=datetime(2023,8,15)
dates_list=[datetime(2023,12,31),
            datetime(2023,8,15),datetime(2023,5,1)]
for i in dates_list:
    if i==given_date:
        print( given_date,"is found in the list at index 1")
        break
else:
    print("Not found")