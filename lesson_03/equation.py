num = int(input("Enter a number : "))
num2 = int(input("Enter a number: "))
oper = input("Choose a number (1, 2, 3, 4): ")
if oper == '1':
    result1 = num + num2
    print(num, '+',num2, '=', result1 )
elif oper == '2':
    result2 = num - num2
    print(num, '-', num2,'=', result2 )
elif oper == '3':
    result3 = num * num2
    print(num, '*',num2, '=', result3 )
elif oper == '4':
    result4 = num / num2
    print(num, '/', num2, '=', result4 )