# There are total 5 data types in python
# 1. Numeric data types
""" Numeric data types are used to store numeric values. There are three numeric data types in Python:
1. int (integer) - used to store whole numbers, e.g., 1, 2, 3
e.g., you can create an integer variable like this: my_int = 10
2. float (floating-point) - used to store decimal numbers, e.g., 1.5, 2.75
e.g., you can create a float variable like this: my_float = 3.14
3. complex - used to store complex numbers, e.g., 1 + 2j 
e.g., you can create a complex variable like this: my_complex = 1 + 2j -output: (1+2j)
"""
# 2. Sequence data types
""" Sequence data types are used to store a collection of items in a specific order. There are three sequence data types in Python:
1. list - a mutable ordered collection of items, e.g., [1, 2, 3]
example, you can create a list of numbers like this: my_list = [1, 2, 3, 4, 5]
2. tuple - an immutable ordered collection of items, e.g., (1, 2, 3)
3. range - represents a sequence of numbers, e.g., range(0, 10)
"""
# 3. Set data types
""" Set data types are used to store a collection of unique items. There is one set data type in Python:
1. set - an unordered collection of unique items, e.g., {1, 2, 3}
for example, you can create a set of numbers like this: my_set = {1, 2, 3, 4, 5}
"""
# 4. Mapping data types
""" Mapping data types are used to store key-value pairs. There is one mapping data type in Python:
1. dict - a collection of key-value pairs, e.g., {"name": "Alice", "age": 30}
2. You can create a dictionary like this: my_dict = {"name": "Alice", "age": 30}
"""
# 5. Boolean data types
""" Boolean data types are used to store logical values. There are two boolean values in Python:
1. True - represents the logical truth
example, you can create a boolean variable like this: is_valid = True
2. False - represents the logical false
example, you can create a boolean variable like this: is_valid = False
"""
# backslash [\n/\t/\r] means new line, tab, and return respectively
story = "My name is Dev Gautam aka Ravishankar Gautam\nI'm learning Python Programming language and I'm enjoying it a lot.\nI want to become a Full Stack Python Developer and I will achieve it for sure Becuase I'm a deligent and hardworking person and I never give up on my dreams." # this is a variable of type string
print(story)

#\t means tab
print("\tDev Gautam aka Ravishankar Gautam") # Output: Dev Gautam aka Ravishankar Gautam

#\r means return
print("Dev Gautam aka Ravishankar Gautam\rDev Gautam aka Ravishankar Gautam") # Output: Dev Gautam aka Ravishankar Gautam

#\n means new line
print("Dev Gautam aka Ravishankar Gautam\nDev Gautam aka Ravishankar Gautam") # Output: Dev Gautam aka Ravishankar Gautam
# Dev Gautam aka Ravishankar Gautam
# Dev Gautam aka Ravishankar Gautam

#\b means backspace
print("Dev Gautam aka Ravishankar Gautam\bDev Gautam aka Ravishankar Gautam") # Output: Dev Gautam aka Ravishankar Gautam

#\a means bell
print("Dev Gautam aka Ravishankar Gautam\aDev Gautam aka Ravishankar Gautam") # Output: Dev Gautam aka Ravishankar Gautam

#\f means form feed
print("Dev Gautam aka Ravishankar Gautam\fDev Gautam aka Ravishankar Gautam") # Output: Dev Gautam aka Ravishankar Gautam

#\v means vertical tab
print("Dev Gautam aka Ravishankar Gautam\vDev Gautam aka Ravishankar Gautam") # Output: Dev Gautam aka Ravishankar Gautam


# String
name = "Dev Gautam aka Ravishankar Gautam" # this is a variable of type string
print("My name is", name) # Output: My name is Dev Gautam aka Ravishankar Gautam
nameshort = name[0:5] # this is a variable of type string
print(nameshort) # Output: Dev G
print(name[0:7]) # Output: Dev Gau
print("- format -",name[-7:-1]) # Output: Gauta

# String length
print("- String length -",len(name)) # Output: 39


# skip/slicing
print("- skip/slicing -",name[0:7:2]) # Output: DvGu

# reverse
print("- reverse -",name[7:5:-1]) # Output: tu

# String functions
print("- String functions -",name.upper()) # Output: DEV GAUTAM AKKA RAVISHANKAR GAUTAM
print("- String functions -",name.lower()) # Output: dev gautam aka ravishankar gautam
print("- String functions -",name.title()) # Output: Dev Gautam Aka Ravishankar Gautam
print("- String functions -",name.capitalize()) # Output: Dev gautam aka ravishankar gautam
print("- String functions -",name.replace("Dev Gautam aka Ravishankar Gautam","Dev Gautam aka Ravishankar Gautam")) # Output: Dev Gautam aka Ravishankar Gautam
print("- String functions -",name.split()) # Output: ['Dev Gautam aka Ravishankar Gautam']
print("- String functions -",name.split(" ")) # Output: ['Dev', 'Gautam', 'aka', 'Ravishankar', 'Gautam']

# String formatting
print("- String formatting -",name.format()) # Output: Dev Gautam aka Ravishankar Gautam
print("- String formatting -",name.format("Dev Gautam aka Ravishankar Gautam")) # Output: Dev Gautam aka Ravishankar Gautam

# String concatenation
print("- String concatenation -",name + " Dev Gautam aka Ravishankar Gautam") # Output: Dev Gautam aka Ravishankar Gautam Dev Gautam aka Ravishankar Gautam

# String multiplication
print("- String multiplication -",name * 2) # Output: Dev Gautam aka Ravishankar Gautam Dev Gautam aka Ravishankar Gautam

# String membership
print("- String membership -","Dev Gautam aka Ravishankar Gautam" in name) # Output: True
print("- String membership -","Dev Gautam aka Ravishankar Gautam" not in name) # Output: False

# String indexing
print("- String indexing -",name[0]) # Output: D
print("- String indexing -",name[-1]) # Output: m
print("- String indexing -",name[0:7]) # Output: Dev Gau
print("- String indexing -",name[0:7:2]) # Output: DvGu
print("- String indexing -",name[7:5:-1]) # Output: tu




num1 = 10  # this is a variable of type integer
num2 = 3.14  # this is a variable of type float 
print(num1 + num2)  # Output: 13.14

nothing = None  # this is a variable of type NoneType
print(nothing)  # Output: None

"""
Variable rules
1. Variable names can only contain letters, numbers, and underscores (_). They cannot start with a number.
2. Variable names are case-sensitive, meaning that 'myVariable' and 'myvariable' are considered different variables.
3. Variable names should be descriptive and meaningful to make the code more readable.
4. Variable names cannot be the same as Python keywords (reserved words).
5. Variable names should not contain spaces. Use underscores (_) to separate words in variable names.
"""