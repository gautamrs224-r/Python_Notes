# Input function in python is used to take input from the user.

'''
This function allows the user to take input from the keyboard as a string.
a = input("enter name") # if a is "harry", the user entered harry
It is important to note that the output of input is always a string (even if a number is entered).
'''

# a = input("Enter Number 1: ")
# b = input("Enter Number 2: ")
# print(a)
# print(b)
# print("a + b = ", a + b) # Output: a + b =  12 if a is 1 and b is 2, why is this happening? Because the input function takes input as a string, so when we add two strings, it concatenates them instead of adding them as numbers.

# To fix this, we can convert the input to an integer using the int() function.
a = int(input("Enter Number 1: "))
b = int(input("Enter Number 2: "))
print("a + b = ", a + b)