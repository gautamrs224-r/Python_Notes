# Tuple Data Types
"""
Tuple data types are used to store a collection of items in a specific order. 
There is one tuple data type in Python:
1. tuple - an immutable ordered collection of items, e.g., (1, 2, 3)
example, you can create a tuple of numbers like this: my_tuple = (1, 2, 3, 4, 5)
"""
# Example of tuple
my_tuple = (1, 2, 3, 4, 5)
print("Type of variable my_tuple is:", type(my_tuple)) # Output: Type of variable my_tuple is: <class 'tuple'>
sec_tuple = (1,)
print("Type of variable sec_tuple is:", type(sec_tuple)) # Output: Type of variable sec_tuple is: <class 'tuple'>

# Creating an empty tuple
empty_tuple = ()
print("Type of variable empty_tuple is:", type(empty_tuple)) # Output: Type of variable empty_tuple is: <class 'tuple'>

# Accessing elements of tuple
print("First element of tuple my_tuple is:", my_tuple[0]) # Output: First element of tuple my_tuple is: 1
print("Last element of tuple my_tuple is:", my_tuple[-1]) # Output: Last element of tuple my_tuple is: 5

# Tuple of Methods
print("Length of tuple my_tuple is:", len(my_tuple)) # Output: Length of tuple my_tuple is: 5
print("Maximum element of tuple my_tuple is:", max(my_tuple)) # Output: Maximum element of tuple my_tuple is: 5
print("Minimum element of tuple my_tuple is:", min(my_tuple)) # Output: Minimum element of tuple my_tuple is: 1

# Tuple Slicing
print("First 3 elements of tuple my_tuple are:", my_tuple[:3]) # Output: First 3 elements of tuple my_tuple are: (1, 2, 3)
print("Last 3 elements of tuple my_tuple are:", my_tuple[-3:]) # Output: Last 3 elements of tuple my_tuple are: (3, 4, 5)

# Tuple Concatenation
concat_tuple = my_tuple + sec_tuple
print("Concatenated tuple is:", concat_tuple) # Output: Concatenated tuple is: (1, 2, 3, 4, 5, 1)

# Tuple Repetition
repeated_tuple = my_tuple * 2
print("Repeated tuple is:", repeated_tuple) # Output: Repeated tuple is: (1, 2, 3, 4, 5, 1, 2, 3, 4, 5)

# Tuple Unpacking
a, b, c, d, e = my_tuple
print("a is:", a) # Output: a is: 1
print("b is:", b) # Output: b is: 2
print("c is:", c) # Output: c is: 3
print("d is:", d) # Output: d is: 4
print("e is:", e) # Output: e is: 5
