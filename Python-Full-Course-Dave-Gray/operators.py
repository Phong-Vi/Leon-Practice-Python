# Arithmetic operators
# + - * / % ** //
x = 2**5    # exponentiation
print(x)

y = 5//2    # floor division
print(y)

z = 5%2     # modulo operator
print(z)

# Comparison operators
# == != > < >= <=
print(5 == 5)
print(5 != 5)
print(5 > 5)

# Logical operators
# and or not
print(True and False)
print(True or False)
print(not True)

# Identity operators
# is is not
print(True is False)
print(True is not False)

# Membership operators
# in not in
print("Hello" in "Hello, World!")
print("Hello" not in "Hello, World!")

# Bitwise operators
# & | ^ ~ << >>
x = 0b1100
y = 0b1010
print(bin(x & y))  # bitwise AND
print(bin(x | y))  # bitwise OR
print(bin(x ^ y))  # bitwise XOR
print(bin(~x))     # bitwise NOT
print(bin(x << 2))  # bitwise left shift
print(bin(x >> 2))  # bitwise right shift

# Assignment operators
# = += -= *= /= %= **= //= &= |= ^= ~= <<= >>=
x = 5
x += 5
print(x)

# Operator precedence
# ()
# ** (exponentiation)
# +x, -x, ~x (unary plus, unary minus, bitwise NOT)
# *, /, //, % (multiplication, division, floor division, modulo)
# +, - (addition, subtraction)
# <<, >> (bitwise shift operators)
# & (bitwise AND)
# ^ (bitwise XOR)
# | (bitwise OR)
# ==, !=, >, <, >=, <=, is, is not, in, not in (comparison, identity, membership operators)
# not (logical NOT)
# and (logical AND)
# or (logical OR)
# =, +=, -=, *=, /=, %=, **=, //=, &=, |=, ^=, ~=, <<=, >>= (assignment operators)
# , (comma operator)
# lambda (lambda expression)


# if - else (conditional expression)
x = 5
y = 10
z = x if x > y else y
print(z)

# if - elif - else
x = 5
y = 10
if x > y:
    print("x is greater than y")
elif x < y:
    print("x is less than y")
else:
    print("x is equal to y")