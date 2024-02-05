# Read file , validate password with valid complexity and write them to another file
input_file="C:\\Users\\Maysoon Sobhy\\Documents\\read_passwords.txt.txt"
output_file="C:\\Users\\Maysoon Sobhy\\Documents\\valid_passwords.txt.txt"
count_lower,count_upper,count_special,count_digits=0,0,0,0
with open(input_file,"r") as my_input_file:
    input_f=my_input_file.read()
with open(output_file, "w") as my_output_file:
    my_output_file.write(input_f)
if (len(my_output_file)>=8):
    for letter in input_f:
        if letter.islower():
            count_lower=count_lower+1
        elif letter.isupper():
            count_upper=count_upper+1
        elif letter.isnumeric():
            count_digits=count_digits+1
        elif letter.isalnum():
            count_special=count_special+1
        if (count_lower>=1 and count_upper>=1 and count_special>=1 and count_digits>=1):
            print(my_output_file.write(input_f))







