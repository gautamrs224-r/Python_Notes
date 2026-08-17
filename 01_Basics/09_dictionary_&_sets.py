marks = {
    "Ravishankar": 87,
    "Ravishankar Gautam": 100,
    "Ravishankar Gautam Gautam": 99
}
print(marks, type(marks))
print(marks["Ravishankar"])

# Properties Of Python Dictionaries
# It is unordered.
# It is mutable.
# It is indexed.
# Cannot contain duplicate keys.

# Dictionaries Methods
# clear() - Removes all the elements from the dictionary
data = {
    'name': 'Ravishankar Gautam',
    'age': 21,
    'city': 'Mumbai'
}

data.clear()
print(data)

# copy() - Returns a copy of the dictionary
data.copy()
print(data)

# fromkeys() - Returns a dictionary with the specified keys and value
data.fromkeys(['name', 'age', 'city'])
print(data)

# get() - Returns the value of the specified key
data.get('name')
print(data)

# items() - Returns a list containing a tuple for each key value pair
data.items()
print(data)

# keys() - Returns a list containing the dictionary's keys
data.keys()
print(data)

# pop() - Removes the element with the specified key
data.pop('name')
print(data)

# popitem() - Removes the last inserted key-value pair
data.popitem()
print(data)

# setdefault() - Returns the value of the specified key. If the key does not exist: insert the key, with the specified value
data.setdefault('name')
print(data)

# values() - Returns a list of all the values in the dictionary
data.values()
print(data)

# update() - Updates the dictionary with the specified key-value pairs
data.update({'name': 'Ravishankar Gautam'})
print(data)



# Sets and Methods
'''
Properties Of Sets
Sets are unordered => Element’s order doesn’t matter
Sets are unindexed => Cannot access elements by index
There is no way to change items in sets.
Sets cannot contain duplicate values.
Operations On Sets
Consider the following set:
s = {1,8,2,3}
len(s): Returns 4, the length of the set
s.remove(8): Updates the set s and removes 8 from s.
s.pop(): Removes an arbitrary element from the set and return the element removed.
s.clear(): empties the set s.
s.union({8,11}): Returns a new set with all items from both sets.
s.intersection({8,11}): Returns a set which contains only item in both sets {8}.
'''
# Sets Methods
# add() - Adds an element to the set
data = {1, 2, 3}
data.add(4)
print(data)

# clear() - Removes all the elements from the set
data.clear()
print(data)

# update() - Updates the set with the union of this set and others
data = {1, 2, 3}
data.update({4, 5, 6})
print(data)

# clear() - Removes all the elements from the set
data.clear()
print(data)

# copy() - Returns a copy of the set
data = {1, 2, 3}
data_copy = data.copy()
print(data_copy)

# difference() - Returns a set containing the difference between two or more sets
data = {1, 2, 3}
data2 = {2, 3, 4}
data.difference(data2)
print(data)

# difference_update() - Removes the items in this set that are also included in another, specified set
data = {1, 2, 3}
data2 = {2, 3, 4}
data.difference_update(data2)
print(data)

# discard() - Remove the specified item
data = {1, 2, 3}
data.discard(2)
print(data)

# intersection() - Returns a set, that is the intersection of two other sets
data = {1, 2, 3}
data2 = {2, 3, 4}
data.intersection(data2)
print(data)

# intersection_update() - Removes the items in this set that are not present in other, specified set(s)
data = {1, 2, 3}
data2 = {2, 3, 4}
data.intersection_update(data2)
print(data)

# isdisjoint() - Returns whether two sets have a intersection or not
data = {1, 2, 3}
data2 = {2, 3, 4}
data.isdisjoint(data2)
print(data)

# issubset() - Returns whether another set contains this set or not
data = {1, 2, 3}
data2 = {2, 3, 4}
data.issubset(data2)
print(data)

# issuperset() - Returns whether this set contains another set or not
data = {1, 2, 3}
data2 = {2, 3, 4}
data.issuperset(data2)
print(data)

# union() - Return a set containing the union of sets
data = {1, 2, 3}
data2 = {2, 3, 4}
data.union(data2)
print(data)

# pop() - Removes an element from the set
data = {1, 2, 3}
data.pop()
print(data)

# remove() - Removes the specified element
data = {1, 2, 3}
data.remove(2)
print(data)

# discard() - Remove the specified item
data = {1, 2, 3}
data.discard(2)
print(data)

# symmetric_difference() - Returns a set with the symmetric differences of two sets
data = {1, 2, 3}
data2 = {2, 3, 4}
data.symmetric_difference(data2)
print(data)

# symmetric_difference_update() - inserts the symmetric differences from this set and another
data = {1, 2, 3}
data2 = {2, 3, 4}
data.symmetric_difference_update(data2)
print(data)

# union() - Return a set containing the union of sets
data = {1, 2, 3}
data2 = {2, 3, 4}
data.union(data2)
print(data)

# Important Notes:
# 1. Sets are unordered, so you cannot be sure in which order the items will appear.
# 2. Sets are unindexed, which means that you cannot access them by referring to an index.
# 3. Sets are unchangeable, meaning that you cannot change the items in a set once it has been created.
# 4. Sets cannot contain duplicate items.
# 5. Sets are mutable, which means that you can add or remove items from a set after it has been created.
# 6. Sets are iterable, which means that you can loop through the items in a set.
