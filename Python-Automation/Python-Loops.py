# *** while ***
# while True:
#     print("Enter your name:")
#     name = input()
#     if name == 'your name':
#         break
# print("Thank you!");

# i = 0;
# while (i < 10):
#     print(i);
#     i += 1;
# print("Done with loop");

# def attempts(n):
#     i = 1;
#     while i <= n:
#         print("Attempt", i);
#         i += 1;
#     print("Done");

# attempts(5);

# def get_username():
#     return input("Enter username: ");

# def is_username_valid(username):
#     if len(username) < 3:
#         return False;
#     if len(username) > 15:
#         return False;
#     return True;

# username = get_username();
# while not is_username_valid(username):
#     print("Invalid username");
#     username = get_username();
# print("Username is valid");

# *** for ***
# for i in range(5):
#     print(i);
# for i in range(3, 10):
#     print(i);
# for i in range(0, 10, 2):
#     print(i);
# for i in range(10, 0, -1):
#     print(i);

# friends = ["Kevin", "Karen", "Jim", "Oscar", "Toby"];
# for friend in friends:
#     print(friend);

# values = [10, 20, 30];
# total = 0;
# for value in values:
#     total += value;
# print(total);

# for letter in "Giraffe Academy":
#     print(letter);

# def to_celsius(fahrenheit):
#     return (fahrenheit - 32) * 5/9;

# for x in range(0, 101, 10):
#     print(f"{x} Fahrenheit = {to_celsius(x)} Celsius");

# for left in range(7):
#     for right in range(left, 7):
#         print(f"[{left} | {right}]", end=" ");
#     print();

teams = ["Barcelona", "Real Madrid", "Bayern Munich", "Liverpool", "Manchester City"];
for home_team in teams:
    for away_team in teams:
        if home_team != away_team:
            print(f"{home_team} vs {away_team}");


# *** recursion ***
print("Recursion");
def factorial(n):
    if n == 0:
        print("Base case (1) reached");
        return 1;
    result = n * factorial(n - 1);
    print(f"{result}: Calculating factorial of {n}");
    return result;

print(factorial(5));