# program to read from csv to lists
import csv
persons_list=[]
with open("C:\\my_files\\people.csv","r") as my_file:
    read_from_excel=csv.reader(my_file)
    for row in read_from_excel:
        #print(row[0])
        persons_list.append(row)
print(persons_list)