
# converting a list of tuples to a dictionary
colors_list = [("read",223) ,("blue",201) , ("green",210)]
print("...........converting a list of tuples to a dictionary............")
result ={}
for (key , value) in colors_list:
    result.setdefault(key,[]).append(value)
print(result)
print(".......Method 2.........")
colors_list = [("read",223) ,("blue",201) , ("green",210)]
# converting to dict
result = dict(colors_list)
print(result)
