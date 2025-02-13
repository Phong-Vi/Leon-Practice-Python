# *** Global Scope / Local Scope ***
name = "Dave"

def greeting(firstname):
    color = "Blue"
    print(color)
    print(firstname)
    print(name)

greeting("Phong")

def another():
    """
    Calls the greeting function with the argument "Louis".
    Sets a local variable 'name' to "Léon".
    """
    name = "Léon"   # name is local here so no impact to the global name
    greeting("Louis")

another()

def yet_another():
    """
    Calls the greeting function with the argument "Louis".
    Sets the global variable 'name' to "Léon".
    """
    global name
    name = "Léon"   # name is now the global one
    greeting("Louis")

yet_another()