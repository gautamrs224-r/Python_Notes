# There are different types operators in Python that can be used to perform various operations on variables and values. Here are some of the most commonly used operators:
# 1. Arithmetic operators: +, -, *, / etc.
# 2. Assignment operators: =, +=, -= etc.
# 3. Comparison operators: ==, >, >=, <, != etc.
# 4. Logical operators: and, or, not.

# 1. Arithmetic operators
a = 10
b = 3
print("addition:", a + b) # Output: addition: 13
print("subtraction:", a - b) # Output: subtraction: 7
print("multiplication:", a * b) # Output: multiplication: 30
print("division:", a / b) # Output: division: 3.3333333333333335

# 2. Assignment operators
x = 5
x += 3  # equivalent to x = x + 3
print("x after += 3:", x) # Output: x after += 3: 8

y = 10
y -= 2  # equivalent to y = y - 2
print("y after -= 2:", y) # Output: y after -= 2: 8

z = 4
z *= 2  # equivalent to z = z * 2
print("z after *= 2:", z) # Output: z after *= 2: 8

a = 16
a /= 4  # equivalent to a = a / 4
print("a after /= 4:", a) # Output: a after /= 4: 4.0

b = 9
b %= 4  # equivalent to b = b % 4
print("b after %= 4:", b) # Output: b after %= 4: 1

c = 2
c **= 3  # equivalent to c = c ** 3
print("c after **= 3:", c) # Output: c after **= 3: 8

d = 10
d //= 3  # equivalent to d = d // 3
print("d after //= 3:", d) # Output: d after //= 3: 3

e = 5
e &= 3  # equivalent to e = e & 3
print("e after &= 3:", e) # Output: e after &= 3: 1

f = 6
f |= 3  # equivalent to f = f | 3
print("f after |= 3:", f) # Output: f after |= 3: 7

g = 5
g ^= 3  # equivalent to g = g ^ 3
print("g after ^= 3:", g) # Output: g after ^= 3: 6

h = 8
h >>= 2  # equivalent to h = h >> 2
print("h after >>= 2:", h) # Output: h after >>= 2: 2

i = 4
i <<= 1  # equivalent to i = i << 1
print("i after <<= 1:", i) # Output: i after <<= 1: 8


# 3. Comparison operators
x = 5
y = 10
print("x == y:", x == y) # Output: x == y: False
print("x != y:", x != y) # Output: x != y: True
print("x > y:", x > y) # Output: x > y: False
print("x < y:", x < y) # Output: x < y: True
print("x >= y:", x >= y) # Output: x >= y: False
print("x <= y:", x <= y) # Output: x <= y: True


# 4. Logical operators
a = True
b = False
print("a and b:", a and b) # Output: a and b: False
print("a or b:", a or b) # Output: a or b: True
print("not a:", not a) # Output: not a: False
print("not b:", not b) # Output: not b: True


# Type of variable
user_name = "Dev Gautam"
t = type(user_name)
print("Type of variable user_name is:", t) # Output: Type of variable user_name is: <class 'str'>

user_age = 25
t = type(user_age)
print("Type of variable user_age is:", t) # Output: Type of variable user_age is: <class 'int'>

user_height = 5.9
t = type(user_height)
print("Type of variable user_height is:", t) # Output: Type of variable user_height is: <class 'float'>

# Tpyecasting
# Typecasting is the process of converting one data type to another. In Python, you can use the following functions to perform typecasting:
# 1. int() - converts a value to an integer
# 2. float() - converts a value to a floating-point number
# 3. str() - converts a value to a string
# 4. bool() - converts a value to a boolean
# Example of typecasting
x = "10"
y = int(x)
print("Type of variable y is:", type(y)) # Output: Type of variable y is: <class 'int'>
z = float(x)
print("Type of variable z is:", type(z)) # Output: Type of variable z is: <class 'float'>
