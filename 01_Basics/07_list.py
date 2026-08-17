# List
storage = [ 'apple', 'banana', 'cherry', 17, 3.14, True ]

print(storage)
print(storage[0]) # Output: apple
print(storage[1]) # Output: banana
print(storage[2]) # Output: cherry
print(storage[3]) # Output: 17
print(storage[4]) # Output: 3.14
print(storage[5]) # Output: True

# List Methods
print(storage.index('cherry')) # Output: 2
print(storage.count(True)) # Output: 1

# List Slicing
print(storage[0:2]) # Output: ['apple', 'banana']
print(storage[2:]) # Output: ['cherry', 17, 3.14, True]
print(storage[:2]) # Output: ['apple', 'banana']

storage.append('orange') # Output: ['apple', 'banana', 'cherry', 17, 3.14, True, 'orange']
storage.insert(2, 'kiwi') # Output: ['apple', 'banana', 'kiwi', 'cherry', 17, 3.14, True, 'orange']
storage.remove('kiwi') # Output: ['apple', 'banana', 'cherry', 17, 3.14, True, 'orange']
storage.pop() # Output: ['apple', 'banana', 'cherry', 17, 3.14, True]
storage.clear() # Output: []
storage.sort() # Output: ['apple', 'banana', 'cherry', 17, 3.14, True]
storage.reverse() # Output: [True, 3.14, 17, 'cherry', 'banana', 'apple']
storage.append('apple') # Output: ['apple', 'banana', 'cherry', 17, 3.14, True, 'apple']


print(storage)

# Important Notes:
# 1. Lists are mutable
# 2. Lists are ordered
# 3. Lists are indexed
# 4. Lists are iterable