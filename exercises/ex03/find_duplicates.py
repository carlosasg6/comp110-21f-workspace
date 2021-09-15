"""Finding duplicate letters in a word."""

__author__ = "730330989"

da_word: str = str(input("Enter a word: "))
dup: bool = False
i: int = 0
while i < len(da_word):
    char: str = da_word[i]
    j: int = i + 1
    while j < len(da_word):
        if da_word[i] == da_word[j]:
            dup = True
        j += 1
    i += 1
print("Found duplicate: " + str(dup))