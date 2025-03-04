# Variables needed to make an omelette:
eggs: int = input("How many eggs do you want to put into your omelette?\n")

print("You want to use " +eggs+ " eggs in your omelette.")

print(f"Great! Let us make an omelette with {eggs} eggs")

eggs_fridge: int = input("How many eggs do you have in the fridge?\n")

if (eggs <= eggs_fridge):
    print(f"We can go ahead and cook your omelette with {eggs} eggs")
else:
    print(f"I'm afraid there is not enough eggs to cook a {eggs}-eggs omelette!")


#We need some oil of type float
some_oil: float=0.15

#we need a stove
stove: bool = False

#We need some heat
some_heat: float = 0

#We need a pan
pan: bool = False

#We need a "match" ; Attention ! En Python, "match" est un mot réservé
has_match: bool = False

#We need a bowl to beat the eggs
bowl: bool = False

#we need a whisk or a fork to beat the eggs
whisk: bool = False

fork: bool = False

stove = input("Do you have a stove at home? (Y/N)\n")

if (stove=='N' or stove=='n'):
    print("You should buy one stove right away, man!")
else:
    stove = True
    print("Great! Let us see if you have everything else needed to cook the omelette...")

pan = input("Do you have a pan at home? (Y/N)\n")

if (pan=='N' or pan=='n'):
    print("You should buy one pan right away, man!")
else:
    pan = True
    print("Great! Let us see if you have everything else needed to cook the omelette...")

#Pour les allumettes, le nom de la variable boolean est has_match pour éviter d'utiliser le mot réservé "match".
has_match = input("Do you have a match at home? (Y/N)\n") 

if (has_match=='N' or has_match=='n'):
    print("You should buy at least one match right away, man!")
else:
    has_match = True
    print("Great! It seems that you have everything you may need to cook an omelette!")

#Heat the stove
heat_stove = input("Did you heat your stove? (Y/N)\n")

if (heat_stove=='Y' or heat_stove=='y'):
    print(f"Good job! Now, add {some_oil} gram of oil into the pan.")
    beat_eggs = input("Are eggs beaten by your whisk? (Y/N)\n")
    if (beat_eggs=='Y' or beat_eggs=='y'):
        print(f"Great! Now, pour {eggs} the beaten eggs into the oiled pan.")
        print("Congratulations!!! Your omlette will be ready in 1 minute. Enjoy your lunch!")
    else:
        print(f"You should beat {eggs} eggs first with your whisk.")
else:
    print("So, what are you waiting for? Hurry up!")
