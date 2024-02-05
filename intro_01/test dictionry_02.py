# show dictionary basic
# creat dict
shopping_cart_dict ={"milk":48.0 , "bread" :10.0, "eggs":145.0}
print(shopping_cart_dict)
print(type(shopping_cart_dict))

print("..........access element by key......... ")
print("value of key bread=" , shopping_cart_dict["bread"]  )

print("........modify value of key..........")
shopping_cart_dict["bread"]=15
print(shopping_cart_dict)

print("........adding a new key.........")
shopping_cart_dict["nescafe"]=78
print(shopping_cart_dict)

print("........remove item from dict by key........")
shopping_cart_dict.pop("nescafe")
print(shopping_cart_dict)

print("........concate between 2 dict..........")
dict1 = {101:"ahmed",102:"ola",103:"omar"}
dict2 = {104:"ali", 105:"sarah",106:"nada"}
dict1.update(dict2)
print(dict1)