person_tuple =(101 , "Ahmed" , 3000.0 , "Cairo")
print("person name:" + person_tuple[1])
# concatenation
person_job = ("python devolper ", "senoir")
person_tuple = person_tuple +person_job
print(person_tuple)

# looping
for item in person_tuple:
    print(item)

# access
print(person_tuple[2])

print(person_tuple[::-1])