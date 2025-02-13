# Strings are immutable, lists are mutable, dictionaries are mutable.
# name = "Mike";
# print(len(name));   # 4
# print(name[0]);     # M
# print(name[len(name) - 1]); # e
# print(name[1:3]);   # ik
# print(name[:3]);    # Mik
# print(name[1:]);    # ike
# print(name[:]);     # Mike
# print(name[1:100]); # ike

# # name[0] = "N"; # TypeError: 'str' object does not support item assignment

# message = "Hello World";
# print(message.lower()); # hello world
# index = message.index("World");
# print(index); # 6

# def replace_domain(email, old_domain, new_domain):
#     """This function replaces the domain of an email"""
#     if "@" + old_domain in email:
#         index = email.index("@" + old_domain);
#         new_email = email[:index] + "@" + new_domain;
#         return new_email;
#     return email;

# email = "trantanphong.vi@odigo.com"
# old_domain = "odigo.com"
# new_domain = "gmail.com"
# print(replace_domain(email, old_domain, new_domain)); #trantanphong.vi@gmail.com

# print(" yes ".strip()); # yes
# print(" yes ".lstrip()); # yes
# print(" yes ".rstrip()); # yes
# print("yes".strip("s")); # ye

# print("...".join(["yes", "no", "maybe"])); # yes...no...maybe
# print("123".isnumeric()); # True
# print("Forest".endswith("rest")); # True
# print(int("123") + int("456")); # 579
# print("Hello".replace("l", "X")); # HeXXo
# print("Hello".find("l")); # 2
# print("Hello".find("X")); # -1
# print("Hello".count("l")); # 2
# print("Hello".isalpha()); # True
# print("Hello".isalnum()); # True
# print("Hello".islower()); # False
# print("Hello".isupper()); # False
# print("Hello".istitle()); # True
# print("Hello".startswith("H")); # True
# print("Hello".split("l")); # ['He', '', 'o']
# print("Hello".split("e")); # ['H', 'llo']

# name="Mike"
# number=3
# print(f"{name} has {number} apples.") # Mike has 3 apples.
# print("Hello {name}, you have {number} apples.".format(name="Mike", number=3)) # Hello Mike, you have 3 apples.
# print("Hello %s, you have %d apples." % (name, number)) # Hello Mike, you have 3 apples.

# price = 7.5
# with_tax = price * 1.09
# print(f"Base price: ${price}, with tax: ${with_tax:.2f}") # Base price: $7.5, with tax: $8.18
# print("Base price: ${}, with tax: ${:.2f}".format(price, with_tax)) # Base price: $7.5, with tax: $8.18
# print("Double base price: ${price}, with tax: ${with_tax:.2f}".format(with_tax=2*with_tax, price=2*price)) # Double base price: $15.0, with tax: $16.36

# def to_celsius(x):
#     return (x-32)*5/9

# for x in range(0, 101, 10):
#     print("{:>3} F | {:>6.2f} C".format(x, to_celsius(x))) # align right, 3 characters wide, 6 characters wide, 2 decimal places


# Dictionaries are unordered collections of items. While other compound data types have only value as an element, a dictionary has a key: value pair.
# animals = {"dogs": [20, 10, 15, 8, 32, 15], "cats": [3, 4, 2, 8, 2, 4], "rabbits": [2, 3, 3], "fish": [0.3, 0.5, 0.8, 0.3, 1]}
# print(animals["dogs"]) # [20, 10, 15, 8, 32, 15]
# print(animals["dogs"][3]) # 8
# print(animals["fish"]) # [0.3, 0.5, 0.8, 0.3, 1]
# print(animals["fish"][0]) # 0.3

# for k, v in animals.items():
#     print(k, v)

# winners = {1: "Michael", 2: "Tracy", 3: "Tom"}
# for k, v in winners.items():
#     print(f"Position {k}: {v}")

# winners = ["Michael", "Tracy", "Tom"]
# for i, v in enumerate(winners, 1):  # enumerate(iterable, start=0), here start by 1
#     print(f"Position {i}: {v}")

file_counts = {"jpg": 10, "txt": 14, "csv": 2, "py": 23}
for extension, count in file_counts.items():
    print(f"There are {count} files with the .{extension} extension")
print(file_counts.keys()) # dict_keys(['jpg', 'txt', 'csv', 'py'])
print(file_counts.values()) # dict_values([10, 14, 2, 23])
print(file_counts.items()) # dict_items([('jpg', 10), ('txt', 14), ('csv', 2), ('py', 23])
file_counts["cfg"] = 8
print(file_counts) # {'jpg': 10, 'txt': 14, 'csv': 2, 'py': 23, 'cfg': 8}
file_counts["csv"] = 17
file_counts.pop("jpg")
print(file_counts) # {'txt': 14, 'csv': 17, 'py': 23, 'cfg': 8}
file_counts.popitem()
print(file_counts) # {'txt': 14, 'csv': 17, 'py': 23}

def count_letters(text):
    result = {}
    for letter in text:
        if letter.isalpha():
            if letter in result:
                result[letter] += 1
            else:
                result[letter] = 1
    return result
print(count_letters("trantanphong")) # {'t': 2, 'r': 1, 'a': 2, 'n': 2, 'p': 1, 'h': 1, 'o': 1, 'g': 1}

# List of dictionaries
class_points = [{"name": "Michael", "points": 1000}, {"name": "Tracy", "points": 1100}]
for student in class_points:
    print(f"{student['name']} has {student['points']} points")


# Lists are ordered collections of items, dictionaries are unordered collections of items.
# x = ["Now", "we", "are", "cooking!"]
# print(x[0]) # Now
# print(x[3]) # cooking!
# print(x[-1]) # cooking! # last element
# print(x[1:3]) # ['we', 'are']
# print(x[:2]) # ['Now', 'we']
# print(x[2:]) # ['are', 'cooking!']
# print(x.index("are")) # 2
# x.append("vegetables")
# print(x) # ['Now', 'we', 'are', 'cooking!', 'vegetables']
# x.extend(["rice", "tomatoes"])  # x += ["rice", "tomatoes"]
# print(x) # ['Now', 'we', 'are', 'cooking!', 'vegetables', 'rice', 'tomatoes']
# x.insert(0, "first")
# print(x) # ['first', 'Now', 'we', 'are', 'cooking!', 'vegetables', 'rice', 'tomatoes']
# x.remove("rice")
# print(x) # ['first', 'Now', 'we', 'are', 'cooking!', 'vegetables', 'tomatoes']
# x.pop()
# print(x) # ['first', 'Now', 'we', 'are', 'cooking!', 'vegetables']
# x.pop(0)
# print(x) # ['Now', 'we', 'are', 'cooking!', 'vegetables']
# print("are" in x) # True
# print("rice" in x) # False
# print(len(x)) # 5
# y = x.copy()
# print(y) # ['Now', 'we', 'are', 'cooking!', 'vegetables']
# x.clear()
# print(x) # []

# Tuple is a collection which is ordered and unchangeable. Allows duplicate members.
# x = ("Now", "we", "are", "cooking!")
# print(x[0]) # Now
# print(x[3]) # cooking!
# print(x[-1]) # cooking! # last element
# print(x[1:3]) # ('we', 'are')
# print(x[:2]) # ('Now', 'we')
# print(x[2:]) # ('are', 'cooking!')
# print(x.index("are")) # 2
# print("are" in x) # True
# print("rice" in x) # False
# print(len(x)) # 4

# def convert_seconds(seconds):
#     hours = seconds // 3600 # // is integer division
#     minutes = (seconds - hours * 3600) // 60
#     remaining_seconds = seconds - hours * 3600 - minutes * 60
#     return hours, minutes, remaining_seconds
# print(convert_seconds(5000)) # (1, 23, 20)
# print(type(convert_seconds(5000))) # <class 'tuple'>

# def full_emails(people):    #people is a list of tuples
#     result = [] # empty list
#     for email, name in people:
#         result.append(f"{name} <{email}>")
#     return result

# print(full_emails([("toto@gmail.com", "Toto"), ("titi@yahoo.com", "Titi")]))

# classic way of creating a list of multiples of 7
# multiples = []
# for x in range(1, 11):
#     multiples.append(x*7)
# print(multiples)

# list comprehension
# multiples = [x*7 for x in range(1, 11)]
# print(multiples)

# languges = ["Python", "Perl", "Ruby", "Go", "Java", "C"]
# lengths = [len(language) for language in languges]
# print(lengths)

# z = [x for x in range(0, 101) if x % 3 == 0]
# print(z)