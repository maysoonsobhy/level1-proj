#  Solve password validation for rules :
#Minimum 8 characters.
count_upper,count_lower,count_special,count_digits=0,0,0,0
str = "sr@m@_f0rtu9e$._2023"
if (len(str)>=8):
    for letter in str:
        if letter.isupper():
           count_upper=count_upper+1
        elif letter.islower():
         count_lower=count_lower+1
        elif letter.isnumeric():
            count_digits=count_digits+1
        elif letter.isalnum():
            count_special=count_special+1
        elif (count_upper>=1 and count_lower>=1 and count_special>=1 and count_digits>=1):
                print("Valid Password")
        else:
                print("invalid Password")
