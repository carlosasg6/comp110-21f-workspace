"""Counting letters in a string."""

__author__ = "730330989"


# Begin your solution here...
letter: str = str(input("What letter do you want to search for?: "))
the_word: str = str(input("Enter a word: "))

i: int = 0
counter: int = 0
s: str = ""

while i < len(the_word):
    if the_word[i] == letter:
        counter = counter + 1
    i = i + 1
print("Count: " + str(counter))
