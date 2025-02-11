# *** add one each time ***
def add_one(num):
    if (num >= 9):
        return num + 1
    
    total = num + 1
    print(total)

    return add_one(total)

last_number = add_one(0)
print(last_number)

# *** factorial ***
def factorial(n):
    if (n == 1):
        return 1
    return (n * factorial(n-1))

print(factorial(10))