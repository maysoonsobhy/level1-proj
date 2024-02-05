#  Read file and create a list of lines
new_lines_list=[]
with open("C:\\Users\Maysoon Sobhy\Documents\\New Text Document.txt","r") as my_file:
    lines_list=my_file.readlines()
    for line in lines_list:
        line =line.strip() # remove space or new line or tabs
        if line != " ":
            new_lines_list.append(line)
print(new_lines_list)