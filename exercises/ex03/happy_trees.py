"""Drawing forests in a loop."""

__author__ = "730330989"

# The string constant for the pine tree emoji
TREE: str = '\U0001F332'
depth: int = int(input("Depth: "))
i: int = 0
empty: str = ""
while i < depth:
    empty = empty + TREE
    print(empty)
    i += 1