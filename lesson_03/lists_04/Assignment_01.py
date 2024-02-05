# program to calculate sum , count of positive , negative,zeros from list
numbers_list =[-15,16,20,-3,-9,20]
sum_even ,count_even , sum_odd , count_odd , pos_count ,neg_count = 0,0,0,0,0,0

for item in numbers_list :
    if item %2 ==0:
        sum_even = sum_even + item
        count_even = count_even +1
    else:
        sum_odd = sum_odd + item
        count_odd = count_odd +1
print("sum even =" ,sum_even, "count even =",count_even ,"sum odd =", sum_odd,"count odd =",count_odd)
for item in numbers_list:
    if item >=1:
        print("Positive numbers in the list: ", pos_count)
    else:
        print("Negative numbers in the list: ", neg_count)


