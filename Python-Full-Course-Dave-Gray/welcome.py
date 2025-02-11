# *** variables ***
greeting = "Hello, World!"
print(greeting)

# *** functions ***
def greet():
    print("[greet] Hello, World!")  # this is a function that prints a greeting
# greet()  # call the function

# *** classes ***
class Greeter:
    def __init__(self, greeting):
        self.greeting = greeting

    def greet(self):
        print(self.greeting)

greeter = Greeter("[greeter] Hello, World!")
# greeter.greet()

# *** main ***
if __name__ == "__main__":
    greet()
    greeter.greet()
    print("Hello, World!")  # this is the main function that prints a greeting

# *** input ***
name = input("What is your name? ")
print(f"Hello, {name}!")