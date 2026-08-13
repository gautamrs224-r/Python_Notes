# Modules in python are files containing Python code. They can define functions, classes, and variables that you can reuse in other Python programs.

# Comments in Python are use to explain the code and make it more readable. Comments are ignored by the Python interpreter and do not affect the execution of the program.
# Comments has two types
# 1. inline comment
# 2. Multiline comment 
# Pip is a package mangager for Python that allow you to install and manage additional libraries and dependencies that are not included in the standard library.

# I downloaded a module named pyjokes using pip. This module is used to generate random jokes in Python. Let's see how it works.
import pyjokes
joke = pyjokes.get_joke()
print(joke)
