
# Make uppercase half string
str1 = "ArabRepublicOfEgypt"
print("The original string is : " + str(str1))
half_str = len(str1)// 2
result = ""
result = str1[:half_str].lower() + str1[half_str:].upper()
print("The resultant string : " + str(result))
