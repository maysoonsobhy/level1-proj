# write a list data to a csv file.
import csv
people_list=[["name","age","city"],["adham",25,"assuit"],["esam",30,"cairo"],["shady",28,"mansoura"]]
with open("C:\\my_files\\people.csv","w",newline="") as my_file:
    write_to_excel=csv.writer(my_file) #ccv writer
    for person in people_list:
       write_to_excel.writerow(person) #list as argument

