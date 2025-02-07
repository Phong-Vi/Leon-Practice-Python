# Object-oreinted programming in Python
# print(type("Hello World"));

# print("Hello".__add__(" World!"));

# print(dir("Hello World"));

# print(help(str));

# class Apple:
#     pass    # pass is a keyword that does nothing

# constructor, attributes and functions with docstrings
# class Apple:
#     color = ""
#     flavor = ""

#     def __init__(self, color, flavor):
#         """This is a constructor that allows you to create objects from this class"""
#         self.color = color
#         self.flavor = flavor
    
#     def __eq__(self, value):
#         """This is a method that allows you to compare objects from this class"""
#         return self.color == value.color and self.flavor == value.flavor
    
#     def __str__(self):
#         return f"Apple: {self.color} {self.flavor}"

#print(dir(Apple));
#print(help(Apple));

# jonagold = Apple("red", "sweet");
# print(jonagold.color.upper());
# print(jonagold.flavor);

# golden = Apple("yellow", "soft");

# print(golden.__eq__(jonagold));

# print(jonagold);

# Inheritance
# class Fruit:
#     def __init__(self, color, flavor):
#         self.color = color
#         self.flavor = flavor
    
#     def __str__(self):
#         return f"Fruit: {self.color} {self.flavor}"

# class Apple(Fruit):
#     def __str__(self):
#         return "[Apple] " + super().__str__()

# class Grape(Fruit):
#     def __str__(self):
#         return "[Grape] " + super().__str__()

# golden = Apple("yellow", "soft");
# carnelian = Grape("purple", "sweet");
# print(golden);
# print(carnelian);

# class Animal:
#     def __init__(self, name, sound):
#         self.name = name
#         self.sound = sound
    
#     def __str__(self):
#         return f"{self.name} makes {self.sound} sound"

# class Dog(Animal):
#     def __str__(self):
#         return "[Dog] " + super().__str__()

# class Cat(Animal):
#     def __str__(self):
#         return "[Cat] " + super().__str__()

# dog = Dog("Dog", "bark");
# cat = Cat("Cat", "meow");
# print(dog);
# print(cat);

# class Animal:
#     def __init__(self, name, sound):
#         self.name = name
#         self.sound = sound
    
#     def __str__(self):
#         return f"{self.name} makes {self.sound} sound"

# class Dog(Animal):
#     def __str__(self):
#         return "[Dog] " + super().__str__()

# class Cat(Animal):
#     def __str__(self):
#         return "[Cat] " + super().__str__()
    
#     def make_sound(self):
#         return "purr"

# dog = Dog("Dog", "bark");
# cat = Cat("Cat", "meow");
# print(dog);
# print(cat);
# print(f"Cat can also make {cat.make_sound()} sound");

# print(isinstance(dog, Animal));
# print(isinstance(dog, Dog));
# print(isinstance(dog, Cat));

# class Repository:
#     packages = {}   #dictionary

#     def __init__(self, packages):
#         self.packages = packages
    
#     def add_package(self, package, version):
#         self.packages[package] = version
    
#     def remove_package(self, package):
#         del self.packages[package]
    
#     def __iter__(self):
#         return iter(self.packages)
    
#     def __str__(self):
#         return f"Repository with {len(self.packages)} packages"
    
#     def __len__(self):
#         return len(self.packages)
    
#     def __contains__(self, package):
#         return package in self.packages
    
#     def __getitem__(self, key):
#         return self.packages[key]

# myrepo = Repository({"requests": "2.18.4", "numpy": "1.13.1"});
# print(myrepo);
# myrepo.add_package("scipy", "0.19.1");
# print(myrepo);
# for package in myrepo:
#     print(package + " " + myrepo[package]);

# print("requests" in myrepo);
# myrepo.remove_package("requests");
# print("requests" in myrepo);

# Multiple inheritance
class A:
    def __init__(self):
        print("A")
            
    def a(self):
        print("a")
    
class B:
    def __init__(self):
        print("B")
    
    def b(self):
        print("b")

class C(A, B):
    def __init__(self):
        super().__init__()
        print("C")
    
    def a(self):
        print("a from C")
    
    def b(self):
        print("b from C")
    
    def c(self):
        print("c from C")

c = C()
c.a()
c.b()
c.c()

# Modules or Packages
import random
print(random.randint(1, 10))
print(random.choice(["apple", "banana", "cherry"]))

# import datetime
from datetime import date
from datetime import datetime

print(date.today())
phongBirthday = date(1974, 3, 21)
léonBirthday = date(2008, 1, 11)
louisBirthday = date(2011, 5, 8)
print(phongBirthday)
print(phongBirthday.year)
print(phongBirthday.month)
print(phongBirthday.day)
print(phongBirthday.weekday())
print(phongBirthday.isoweekday())
print(phongBirthday.isocalendar())
print(phongBirthday.isoformat())
print(phongBirthday.strftime("%A %d %B %Y %H:%M:%S"))
print(datetime.now())

print(phongBirthday.strftime("%A %d %B %Y"))
print(date.today().year - phongBirthday.year)

print(léonBirthday.strftime("%A %d %B %Y"))
print(date.today().year - léonBirthday.year)

print(louisBirthday.strftime("%A %d %B %Y"))
print(date.today().year - louisBirthday.year)