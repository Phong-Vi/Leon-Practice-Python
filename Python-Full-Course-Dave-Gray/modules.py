# import math
# import sys
# import random as rdm
# from enum import Enum

# print(math.pi)
# print(rdm.choices(["A", "AA", "AAA"]))
# for item in (dir(rdm)):
#     print(item)

# from kansas import randomfunfact
# print(randomfunfact())

import kansas
from rps_game import play_game

print("Welcome to Kansas!")
print(f"  Capital: {kansas.capital.upper()}")
print(f"  Flower: {kansas.flower}")
print(f"  Bird: {kansas.bird}")
print(f"  Song: {kansas.song}")
kansas.randomfunfact()

print(__name__)
print(kansas)

if __name__ == "__main__":
    kansas.randomfunfact()
    play_game()