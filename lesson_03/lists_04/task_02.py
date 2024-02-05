
# join multi tuples into 1 dictionary
print(".........join multi tuples into 1 dictionary........")
person_1_tuples = (101 ,"Ahmed Esam" , 5000.0 ,"Cairo" ,"0127454104")
person_2_tuples = (102 ,"Mohamed Omar" , 6000.0 ,"Alex" , "01147041564")
person_3_tuples = (103 , "Ibrahim Hesham" , 7000.0 ,"Portsaid" , "01032659870")
key_tuple = (101 , 5000.0 , 102 , 6000.0 ,103 , 7000.0)
value_tuple = ("Ahmed Esam" , "Cairo" ,"0127454104","Mohamed Omar","Alex","o1147041564","Ibrahim Hesham","Portsaid","01032659870")
result = {}
for i in range(len(key_tuple)):
    result[key_tuple[i]] = value_tuple[i]
print(str(result))