
# Write a program that asks the user for password using else block
count=0
C_password="python"
password=""
while password!= C_password and count<3:
    password=input("Enter the password:")
    if password==C_password:
        print("Correct password")
    count=count+1
else:
     print("Sorry!,incorrect password")
