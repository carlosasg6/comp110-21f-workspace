"""Example of looping through all characters in a string."""

user_string: str = input("Give me a string! ")

# variable i is a common counter variable name in programming ("Short for iteration or iterator, a counting variable")

i: int = 0

while i < len(user_string):
    print(user_string[i])
    i = i + 1

print("Done!")