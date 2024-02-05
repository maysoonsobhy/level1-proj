# program to read from a text file as a string
my_file = open("C:\\Users\Maysoon Sobhy\Documents\\New Text Document.txt","r")
file_content=my_file.read()
print(file_content)
my_file.close()

print("........read using with clause..........")
with open("C:\\Users\\Maysoon Sobhy\Documents\\New Text Document.txt","r") as my_file:
    file_content=my_file.read()
print(file_content)