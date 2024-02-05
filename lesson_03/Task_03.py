
# library example
book_dict = {"pages":277 , "name":"Gone girl" , "year": 2007}
print(".......Adding New element to dict........")
book_dict["author"] ="Gillian Flynn"
print(book_dict)
print(".........Access element by key.........")
print("value of the key name = ", book_dict["name"]  )
print("........changing element in dict........")
book_dict["year"] = 2010
print(book_dict)
print(".........loop over key , values...........")
for key , value in book_dict.items():
    print(key , value)


print(".........Remove item from dict by key........")
book_dict.pop("name")
print(book_dict)
