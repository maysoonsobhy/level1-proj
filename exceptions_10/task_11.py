
# Write a program that iterates through a list of tuples using else block and handling exception
S_list=[("Ahmed",43),("Adam",22),("Mohammed",87),("Ali",65)]
high_score = S_list[0]
try:
   for i in range(len(S_list)):
      if S_list[i] > high_score:
        high_score=S_list[i]
        print(high_score)
   else:
       ("No high score")
finally:
    ("The list is empty.")
