# program to write text into file
my_file=open("C:\\Users\Maysoon Sobhy\\Documents\\write.txt","w")
my_file.write("i like programming"+"\n")
my_file.write("python is oop language"+"\n")
my_file.write("python is full of libraries")
my_file.close()

print(".......write to file using with clause : no close........")
with open("C:\\Users\\Maysoon Sobhy\\Documents\\write.txt","a") as my_file:
    my_file.write("\ni live in cairo" + "\n")
    my_file.write("i live in alex" + "\n")
    my_file.write("i live in aswan")