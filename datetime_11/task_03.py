

# Check if a specific date falls between two provided dates.
from datetime import datetime
start_date =datetime(2023,1,1)
end_date=datetime(2023,12,31)
given_date=datetime(2023,6,15)
if given_date>start_date<end_date:
        print("the date is in range")
else:
    ("Not in range")