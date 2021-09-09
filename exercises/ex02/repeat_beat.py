"""Repeating a beat in a loop."""

__author__ = "730330989"


# Begin your solution here...
beat: str = str(input("What beat do you want to repeat? "))
times: int = int(input("How many times do you want to repeat it? "))
i: int = 0
empty: str = ""
if times <= 0:
    print("No beat...")
else:
    while i < times:
        i = i + 1
        empty = empty + beat + " "

print(empty)