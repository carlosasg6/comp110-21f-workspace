"""Program that outputs one of at least four random, good fortunes."""

__author__ = "730330989"

# The randint function is imported from the random library so that
# you are able to generate integers at random.
# 
# Documentation: https://docs.python.org/3/library/random.html#random.randint
#
# For example, consider the function call expression: randint(1, 100)
# It will evaluate to an int value >= 1 and <= 100. 
from random import randint


# Begin your solution here...
rando: int = int(randint(1, 4))

print("Your fortune cookie says...")

if rando == 1:
    print("You will have a very lucky month!")
else:
    if rando == 2:
        print("You are to meet a new mysterious person soon, be friendly!")
    else:
        if rando == 3:
            print("You will soon experience a bound of unexpected wealth, use it wisely.")
        else:
            print("Take a moment to practice your appreciation.")
print("Now go spread positive vibes!")
