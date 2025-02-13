# String,integer,float,boolean
# print(str(14) + " is my favorite number");
# print(type(str(14)));
# print(type(14.5));
# print(type(14));
# print(type(True));

# Functions
# def say_hi():
#     print("Hello user");
# say_hi();

# def greet_user(name):
#     print("Hello " + name);
# greet_user("Mike");

# def greeting(name, age):
#     print("Hello " + name + ", you are " + str(age));
# greeting("Mike", 35);

# def cube(num):
#     return num*num*num;
# result = cube(4);
# print(result);

# def max_num(num1, num2, num3):
#     if num1 >= num2 and num1 >= num3:
#         return num1;
#     elif num2 >= num1 and num2 >= num3:
#         return num2;
#     else:
#         return num3;
# print(max_num(3, 4, 5));

# def convert_to_celsius(fahrenheit):
#     return (fahrenheit - 32) * 5/9;
# fahrenheit = 32;
# print(f"fahrenheit {fahrenheit} -> celsius {convert_to_celsius(fahrenheit)}");
# fahrenheit = 100;
# print(f"fahrenheit {fahrenheit} -> celsius {convert_to_celsius(fahrenheit)}");

# def convert_seconds_to_minutes_and_hours(seconds):
#     return seconds, seconds / 60, seconds / 3600;
# seconds = 1200;
# seconds, minutes, hours = convert_seconds_to_minutes_and_hours(seconds);
# print(f"seconds {seconds} -> minutes {minutes} -> hours {hours}");

# def circle_area(radius):
#     return 3.14 * radius * radius;
# radius = 10;
# print(f"radius {radius} -> area {circle_area(radius)}");

# Comparison Operators
# print(3 == 3);
# print(3 == 4);
# print(3 != 4);
# print(3 != 3);
# print(3 > 4);
# print(3 < 4);
# print(3 >= 4);
# print(3 <= 4);
# print(3 == "3");
# print(not(3 == 3));

# Branching
def hint_username(username):
    """This function checks if the username is valid"""
    if len(username) < 3:
        print("Invalid username. Must be at least 3 characters long.");
    elif len(username) > 15:
        print("Invalid username. Must be at most 15 characters long.");
    else:
        print("Valid username");
hint_username("Mike");
hint_username("Mi");
hint_username("MikeMikeMikeMike");

def is_even(number):
    if number % 2 == 0:
        return True;
    return False;
print(is_even(4));
print(is_even(5));