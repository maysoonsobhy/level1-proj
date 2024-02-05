# show function use
def print_numbers(max_value): # function parameter [function input]
  sum = 0
  for i in range (1,max_value):
   print(i , end=" ")
   sum = sum +i
  return sum
print()

# main program
print("main program")
# call the function(sub program)
sum_result =print_numbers(11)