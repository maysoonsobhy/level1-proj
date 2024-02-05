
# loop over all keys and raise the prices 10%
shopping_cart_dict ={"milk":48.0 , "bread" :10.0, "eggs":145.0}
#result={}
#result = {key: float(value) *0.1 for key, value in shopping_cart_dict.items()}
#print(result)

for product , price in shopping_cart_dict.items():
    print(product , price*.1)

