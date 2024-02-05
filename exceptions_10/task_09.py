
# Program to write a function find_prime_num using else block
def find_prime_numbers(a,b):
    for i in range(8,10):
        if i==1:
            return True
        elif i % b ==0:
            return False
            break
    else:
        print("Not found prime number")
print(find_prime_numbers(8,10))
