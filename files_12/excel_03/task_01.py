# Read a csv file and calculate the average value from a specific column
import csv
list=[]
with open("C:\\my_files\\file.csv.xlsx","r")as my_file:
    reader=csv.reader(my_file)
    for row in reader:
        list.append(row)
print(reader)
print(sum(list[1]/len(list[1])))

