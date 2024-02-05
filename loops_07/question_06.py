shopping_cart_dict = {'milk': 20.0, 'bread': 10.0, 'eggs': 145.0}
total_order = 0
for item, value in shopping_cart_dict.items():
    shopping_cart_dict[item] = value + value * 0.1
    total_order = total_order + shopping_cart_dict[item]

print(shopping_cart_dict)
print(total_order)
order_net_salary = total_order + total_order * 0.14
print(order_net_salary)
