# program to read from csv ,filter by cairo ,write an another csv
import csv
persons_list=[]
with open("C:\\my_files\\people.csv","r") as my_file,\
        open("C:\\my_files\\people-filter.csv","w",newline="")as my_file2:
    read_from_excel=csv.reader(my_file)
    write_to_excel=csv.writer(my_file2)
    write_to_excel.writerow(["name","age","city"])
    for row in read_from_excel:
        if row[2]=="cairo":
            #print(row)
            write_to_excel.writerow(row)