# program for students degree
Degree = float(input("enter your degree"))
if Degree >= 90:
    print("You got an A Grade")
elif Degree < 90 and Degree >= 80:
    print("You got an B grade")
elif Degree < 80 and Degree >= 70:
    print("You got an C grade")
elif Degree < 60 and Degree >=50:
    print("You got an D grade")
elif Degree < 50:
    print("You got an F grade")
else:
    print("Invalid")