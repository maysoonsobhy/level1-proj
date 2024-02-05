# program to write a list into a file
my_list=["cairo","alex","aswan"]

with open("C:\\Users\Maysoon Sobhy\\Documents\\write.txt","w")as my_file:

    # loop over the list
    for i in range(len(my_list)):
        if i == len(my_list) -1: # the last turn
            my_file.write(my_list[i])
        else:
            my_file.write(my_list[i]+"\n")


