# this will show how to use datetime in python
import calendar
from datetime import datetime
from dateutil.relativedelta import relativedelta
print("........get today time........")
today=datetime.now()
print(today)
print(".......get date or time or month or year or hours or minutes or second........")
print(today.date())
print(today.date().day)
print(today.date().month)
print(today.date().year)
print(today.time())
print(today.time().hour)
print(today.time().minute)
print(today.time().second)
print("............formatting dates convert from datetime to str , using function strftime() function.............")
print(type(today))
print(today.strftime("%d-%m-%Y-%y"))
print(today.strftime("%b-%B"))
print(today.strftime("%a-%A"))
print(today.strftime("%H-%M-%S")) #time in 24 formats
print(today.strftime("%I-%p"))
print("..........to get custom date - 24 may 2023........")
print("......1. way: using datetime class object.....")
custom_date=datetime(2023,5,24)
print(custom_date)
print(type(custom_date))
print(".......2.way: using date as str variable, convert from str to datetime,using function strptime() ........")
new_custom_date="24-5-2023"
print(type(new_custom_date))
new_custom_date=datetime.strptime(new_custom_date,"%d-%m-%Y")
print(new_custom_date)
print(type(new_custom_date))
print(".......comparison between dates.........")
print(today.date(),custom_date.date())
if today > custom_date:
    print("today is newer than custom date")
elif today < custom_date:
    print("today is older than custom date")
else:
    print("date are equal")
print("........Get the difference between 2 dates as a total.........")
days_difference= today - custom_date
print("Difference between 2 dates=" , days_difference.days)
print("......Get the difference between 2 dates in years,months,days....")
print(today.date(),custom_date.date())
difference = relativedelta(today,custom_date)
print(difference)
print("years=",difference.years,"month=",difference.months,"days=",difference.days)
print("......Adding or subtracting 2 years, 4 months, 10 days on a date..........")
print(today)
new_date=today+relativedelta(years=2 , months=4,days=10)
print(new_date)
print(".......Get the first day | last day of current month......")
first_day=today+ relativedelta(day=1,month=11)
last_day= today + relativedelta(day=31)
print(first_day)
print(last_day)
print("...........find the nearst sunday from today............")
nearest_sunday=today+relativedelta(weekday=calendar.SUNDAY)
print(nearest_sunday)
print("..........find the nearest 2nd sunday from today........ ")
nearest_2ndsunday=today+relativedelta(weekday=calendar.SUNDAY,weeks=1)
print(nearest_2ndsunday)
print("...........find the first sunday from the beginning of the current month.......")
nearest_currmonth_sunday=today+relativedelta(weekday=calendar.SUNDAY,day=1)
print(nearest_currmonth_sunday)
print(".........find the first sunday from the beginning of the next month.......")
nearest_nextmonth=today+relativedelta(weekday=calendar.SUNDAY,months=1,day=1)
print(nearest_nextmonth)
print("..........find the first sunday from the beginning of current year.....")
current_year_sun=today+relativedelta(weekday=calendar.SUNDAY,day=1,month=1)
print(current_year_sun)
print(".........find the first sunday from the beginning of the next year........")
next_year_sun=today+relativedelta(weekday=calendar.SUNDAY,years=1,month=1,day=1)
print(next_year_sun)
