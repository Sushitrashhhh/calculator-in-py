# Python CALCULATOR

operator = input("Enter an operator (+,-,*,/): ")

num1 = int(input('Enter the first number: '))
num2 = int(input('Enter the second number: '))

#print(num1 + num2)

if operator == '+':
    result = num1 + num2
    print(result)
elif operator == '-':
    result = num1 - num2
    print(result)
elif operator == '*':
    result = num1 * num2
    print(result)
elif operator == '/':
    result = num1 / num2
    print(result)     
else:
    print(f"{operator} is not a valid operator")         