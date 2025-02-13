# In Python, a closure is a function object that has access to variables
# in its lexical scope, even when the function is called outside that scope.
# Closures are created by defining a function inside another function and
# then returning the inner function.

# Here's an example to illustrate closures:
def outer_function(msg):
    def inner_function():
        print(msg)
    return inner_function

# Create a closure
closure = outer_function("Hello, World!")
closure()  # Output: Hello, World!

# In this example:
# 1. outer_function takes a parameter msg and defines an
#    inner function inner_function that prints msg.
# 2. outer_function returns inner_function.
# 3. When outer_function is called with the argument "Hello, World!",
#    it returns inner_function, which retains access to the msg variable.
# 4. Calling closure() prints the message "Hello, World!".

# Closures are useful for creating function objects with some preserved state.

# players = {}    # global variable (dictionaires)
def parent_function(person, coins):
    # coins = 3
    players = {}

    def play_game():
        # global players
        nonlocal coins
        nonlocal players
        if (person in players):
            players[person]["played_games"] += 1
        else:
            players[person] = {"initial_coins": coins, "played_games": 1}
        
        coins -= 1
        if coins > 1:
            print("\n" + person + " has " + str(coins) + " coins left.")
        elif coins == 1:
            print("\n" + person + " has " + str(coins) + " coin left.")
        else:
            print("\n" + person + " has is out of coins.")
    
        for player, game in players.items():
            print(f"Player: {player}, Status: {game}")
        
    return play_game

tommy = parent_function("Tommy", 7)
jenny = parent_function("Jenny", 5)
mary = parent_function("Mary", 3)

tommy()

tommy()

jenny()

tommy()

mary()

jenny()

tommy()