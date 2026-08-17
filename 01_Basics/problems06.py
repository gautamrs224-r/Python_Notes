# 1. Write a program to store seven fruits in a list entered by the user.
fruits = []
f1 = fruits.append(input("Enter 1st fruit: "))
f2 = fruits.append(input("Enter 2nd fruit: "))
f3 = fruits.append(input("Enter 3rd fruit: "))
f4 = fruits.append(input("Enter 4th fruit: "))
f5 = fruits.append(input("Enter 5th fruit: "))
f6 = fruits.append(input("Enter 6th fruit: "))
f7 = fruits.append(input("Enter 7th fruit: "))
print(fruits)

# 2. Write a program to accept marks of 6 students and display them in a sorted manner.
marks = []
f1 = marks.append(int(input("Enter 1st fruit: ")))
f2 = marks.append(int(input("Enter 2nd fruit: ")))
f3 = marks.append(int(input("Enter 3rd fruit: ")))
f4 = marks.append(int(input("Enter 4th fruit: ")))
f5 = marks.append(int(input("Enter 5th fruit: ")))
f6 = marks.append(int(input("Enter 6th fruit: ")))
f7 = marks.append(int(input("Enter 7th fruit: ")))
marks.sort()
print(marks)

# 3. Check that a tuple type cannot be changed in python.
tuple = [13, "apple", 3.12, True]
print(type(tuple))


# 4. Write a program to sum a list with 4 numbers.
nums = [17, 22, 63, 43]
sum = nums[0] + nums[1] + nums[2] + nums[3]
print(sum)

# 5. Write a program to count the number of zeros in the following tuple:
a = (7, 0, 8, 0, 0, 9)
count = a.count(0)
print(count)

# 6. Write a program to display a user entered name followed by Good Afternoon using
# input() function.
name = input("Enter your name: ")
print("Good Afternoon", name)
