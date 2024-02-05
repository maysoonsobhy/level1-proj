import calendar
from datetime import datetime
from dateutil.relativedelta import relativedelta
import csv
import os
input_file="C:\\my_files\\Contracts.csv"
output_file="C:\\my_files\\Company.csv"

contract_startdate=""
with open(input_file,"r") as my_file,open(output_file,"w",newline="") as write_to_file:
    reader=csv.reader(my_file)
    writer=csv.writer(write_to_file)
    for row in reader:
        row[1]=installment_date=relativedelta(weekday=calendar.FRIDAY)
        list = (["installment serial", "installment date", "installment amount", "max grace date"],
                [1, installment_date])
        writer.writerow(row)

