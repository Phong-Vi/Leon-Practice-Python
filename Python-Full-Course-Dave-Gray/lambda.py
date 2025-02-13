# A lambda function in Python is a small anonymous function defined
# using the lambda keyword. Lambda functions can have any number of
# arguments but only one expression. They are often used for short,
# simple functions that are not reused elsewhere.

# The syntax for a lambda function is: lambda arguments: expression

# Here is an example of a lambda function that adds two numbers:
add = lambda x, y: x + y
print(add(2, 3))  # Output: 5

# Lambda functions are commonly used with functions like
# map(), filter(), and sorted(). For example:

# Using lambda with map()
numbers = [1, 2, 3, 4]
squared = map(lambda x: x ** 2, numbers)
print(list(squared))  # Output: [1, 4, 9, 16]

# Using lambda with filter()
even_numbers = filter(lambda x: x % 2 == 0, numbers)
print(list(even_numbers))  # Output: [2, 4]

# Using lambda with sorted()
points = [(1, 2), (3, 1), (5, -1)]
sorted_points = sorted(points, key=lambda point: point[1])
print(sorted_points)  # Output: [(5, -1), (3, 1), (1, 2)]

# *** Dave Gray ***
squared_2 = lambda num: num * num
print(squared_2(7))

addTwo = lambda num: num + 2
print(addTwo(7))

addition = lambda a, b: a + b
print(addition(4, 5))

#######################################
def funcBuilder(x):
    return lambda num: num + x

addTen = funcBuilder(10)
addTwenty = funcBuilder(20)

print(addTen(7))
print(addTwenty(7))

#######################################
lambda num: num * num
numbers = [3, 7, 12, 18, 20, 21]
squared_nums = map(lambda num: num*num, numbers)
print(list(squared_nums))

#######################################
lambda num: num % 2 != 0
odd_nums = filter(lambda num: num % 2 != 0, numbers)
print(list(odd_nums))


from functools import reduce
lambda acc, curr: acc + curr
numbers = [1,2,3,4,5,1]
total = reduce(lambda acc, curr: acc + curr, numbers, 10)
print(total)
print(sum(numbers, 10))

#######################################
lambda acc, curr: acc + len(curr)
names = ['Dave Gray', "Sara Ito", 'John Jacob Jingleheimerschmidt']
char_count = reduce(lambda acc, curr: acc + len(curr), names, 0)
print(char_count)