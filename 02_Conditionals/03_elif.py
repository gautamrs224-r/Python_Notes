# using elif statement

num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))
operator = input("Enter operator (+, -, *, /): ")

if operator == '+':
    result = num1 + num2
elif operator == '-':
    result = num1 - num2
elif operator == '*':
    result = num1 * num2
elif operator == '/':
    result = num1 / num2
else:
    print("Invalid operator")

print(num1, operator, num2, "=", result)


# Drives Age Checker

age = int(input("Enter your age here :"))

if( age >= 18):
    print("You are the above the Age. You can drive.")
elif( age >= 16 and age <= 17):
    print("You are the above the Age. You can drive.")
elif( age < 18):
    print("You are the below the Age. You can't drive.")
else:
    print("Invalid Age.")