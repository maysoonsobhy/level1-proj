# program to read from text file and write the content to another text
input_file="C:\\Users\Maysoon Sobhy\Documents\\New Text Document.txt"
output_file="C:\\Users\Maysoon Sobhy\\Documents\\write.txt"
with open(input_file,"r") as my_input_file:
    content=my_input_file.read()
with open(output_file,"w") as my_output_file:
    my_output_file.write(content)