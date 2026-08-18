# 1. Write a program to create a dictionary of Hindi words with values as their English translation. Provide user with an option to look it up!
# Using dictionary
dictionary = {
    "हिंदी": "Hindi",
    "पंजाबी": "Punjabi",
    "मानव": "Bengali",
    "अंग्रेजी": "English"   
}

word = input("Enter a word in Hindi: ")
print("The meaning of", word, "is:", dictionary[word])


# 2. Write a program to input eight numbers from the user and display all the unique numbers (once).
set1 = set()
num = input("Enter 8 numbers: ")
set1.add(num)
print(set1)

# 3. Can we have a set with 18 (int) and '18' (str) as a value in it?
s = set()
s.add(18)
s.add("18")
print(s)


# 4. What will be the length of following set s:
s = set()
s.add(20)
s.add(20.0)
s.add('20') # length of s after these operations?
print(len(s))

# 5. 
s = {}
# What is the type of 's'?
print(type(s)) # Output: <class 'dict'>


# 6. Create an empty dictionary. Allow 4 friends to enter their favorite language as value and use key as their names. Assume that the names are unique.
d = {}
name = input("Enter your name: ")
language = input("Enter your favorite language: ")
d[name] = language
print(d)
# Output: {'Ravishankar': 'Python', 'Ravishankar': 'Python'}


# 7. If the names of 2 friends are same; what will happen to the program in problem 6?
friend1 = "Ravishankar"
friend2 = "Ravishankar"
d[friend1] = "Python"
d[friend2] = "Python"
print(d)
# Output: {'Ravishankar': 'Python', 'Ravishankar': 'Python'}


# 8. If languages of two friends are same; what will happen to the program in problem 6?
friends = ["Ravishankar", "Ravishankar"]
d[friends[0]] = "Python"
d[friends[1]] = "Python"
print(d)
# Output: {'Ravishankar': 'Python', 'Ravishankar': 'Python'}['Ravishankar', 'Ravishankar']

# 9. Can you change the values inside a list which is contained in set S?
s = {8, 7, 12, "Harry", [1,2]}
s[1] = "Ravishankar"
print(s)
# Output: TypeError: 'set' object does not support item assignment  

