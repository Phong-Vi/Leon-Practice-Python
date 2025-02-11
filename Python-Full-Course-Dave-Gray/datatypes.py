# *** data types in python ***

# 1. int
# x = 5
# print(type(x))
# print(isinstance(x, int))
# print(type(x) is int)

# 2. float
import math
# y = 5.00001
# print(type(y))
# print(isinstance(y, float))
# print(type(y) is float)
# print(math.isclose(x, y))   # default rel_tol=1e-9
# print(math.isclose(x, y, rel_tol=1e-9))
# print(math.floor(y))

# 3. complex
# c = 5 + 3j  # 5 + 3i
# print(type(c))
# print(isinstance(c, complex))
# print(type(c) is complex)
# print(c.real)
# print(c.imag)
# print(c.conjugate())

# 4. bool
# t = True
# f = False
# print(type(t))
# print(isinstance(t, bool))
# print(type(t) is bool)
# print(t and f)
# print(t or f)

# 5. str
# name = "Dave"
# print(name + " Gray")
# print(name * 3)
# print(name[0] + str(x))

# multiline = """This is a
# multi-line string
#    Hello, World!
#      How to print a multi-line string in Python"""
# print(multiline)

# print('I\'m Dave')
# print("I'm Dave")
title = "menu".upper()
print(title.center(20, "="))
print("Coffee".ljust(16, ".") + "$1".rjust(4))
print("Muffin".ljust(16, ".") + "$1".rjust(4))
print("Cheesecake".ljust(16, ".") + "$4".rjust(4))
print("Burger".ljust(16, ".") + "$12".rjust(4))

# 6. list
names = ["Bob", "Tod", "Dog"]
for index, name in enumerate(names):
    print(f"{index}: {name}")

# 7. tuple
coordinates = (10, 20, 30)
print(type(coordinates))
print(isinstance(coordinates, tuple))
print(type(coordinates) is tuple)
print(coordinates[0])
print(coordinates[1])
print(coordinates[2])

# Unpacking tuple
x, y, z = coordinates
print(f"x: {x}, y: {y}, z: {z}")

# Single element tuple
single_element_tuple = (5,)
print(type(single_element_tuple))

# 8. set
# 8. set
fruits = {"apple", "banana", "cherry"}
print(type(fruits))
print(isinstance(fruits, set))
print(type(fruits) is set)
print(fruits)

# Adding an element to a set
fruits.add("orange")
print(fruits)

# Removing an element from a set
fruits.remove("banana")
print(fruits)

# Checking membership
print("apple" in fruits)
print("banana" in fruits)

# Set operations
set1 = {1, 2, 3}
set2 = {3, 4, 5}
print(set1.union(set2))
print(set1.intersection(set2))
print(set1.difference(set2))
print(set1.symmetric_difference(set2))

# 9. dict
# 9. dict
person = {
    "name": "Alice",
    "age": 30,
    "city": "New York"
}
print(type(person))
print(isinstance(person, dict))
print(type(person) is dict)
print(person)

# Accessing values
print(person["name"])
print(person.get("age"))

# Adding a new key-value pair
person["email"] = "alice@example.com"
print(person)

# Removing a key-value pair
del person["city"]
print(person)

# Iterating through keys and values
for key, value in person.items():
    print(f"{key}: {value}")

# Checking membership
print("name" in person)
print("city" in person)

# 10. None