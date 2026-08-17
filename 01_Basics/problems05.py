# 1. Write a python program to display a user entered name followed by Good Afternoon using
# input() function.

name = input("Enter your name: ")
print("Good Afternoon", name)

# 2. Write a program to fill in a letter template given below with name and date.
# letter = '''
# Dear <|Name|>,
# You are selected!
# <|Date|>
# '''
letter = "Dear <|Name|>,\nYou are selected!\n<|Date|>"
name = input("Enter your name: ")
date = input("Enter date: ")
letter = letter.replace("<|Name|>", name)
letter = letter.replace("<|Date|>", date)
print(letter)


# 3. Write a program to detect double space in a string.
user_name = input("Enter your name: ")
print(user_name.find("  "))

# 4. Replace the double space from problem 3 with single spaces.
user_name = input("Enter your name: ")
print(user_name.replace("  ", " "))

# 5. Write a program to format the following letter using escape sequence characters.
simple_text = "Hello \nMy name is \nRavishankar Gautam"
print(simple_text)

letter = "Dear Ravishankar Gautam, this python course is nice. Thanks!"
update_letter = "Dear Ravishankar Gautam,\n\tthis python course is nice. \nThanks!"
print(update_letter)

