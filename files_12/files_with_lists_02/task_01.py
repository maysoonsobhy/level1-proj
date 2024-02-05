# Read file , store numbers in a list , and calculate sum and average
new_list=[]
total_sum=0
average=0
with open("C:\\Users\Maysoon Sobhy\\Documents\\read_data_number.txt","r") as my_file:
    lines_list = my_file.readlines()
    for line in lines_list:
        line = line.strip()  # remove space or new line or tabs
        if line != "":
            new_list.append(float(line))
print(new_list)
print(sum(new_list))
print(sum(new_list)/len(new_list))







