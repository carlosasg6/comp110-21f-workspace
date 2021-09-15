"""An exercise in remainders and boolean logic."""

__author__ = "730330989"


# Begin your solution here...
yo_number: int = int(input("Enter an int: "))
if yo_number % 2 == 0:
    if yo_number % 7 == 0:
        print("TAR HEELS")
    else:
        print("TAR")
else:
    if yo_number % 7 == 0:
        print("HEELS")
    else:
        print("CAROLINA")