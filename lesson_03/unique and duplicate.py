list=[1,2,1,2,3,4,5,1,1,2,5,6,7,8,9,9]
uniqueList=[]
duplicateList=[]
for item in list:
    if item not in uniqueList:
        uniqueList.append(item)
    elif item not in duplicateList:
        duplicateList.append(item)
print(uniqueList)
print(duplicateList)
