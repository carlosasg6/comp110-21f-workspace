"""Examples of optional parameters and Union type parameters."""

from typing import Union


def hello(name: Union[str, int, float] = "World") -> str:
    """A delightful greeting funciton."""
    result: str = "Hello, "
    if isinstance(name, str):
        return result + name
    elif isinstance(name, float):
        return result + "alien from sector " + str(name)
    else:
        return result + "COMP" + str(name)


# Calling hello with no arguments leads to use of default value
print(hello())
# Callling hello with one argument overrides the default value
print(hello("John"))
# print(hello(110)) <- This doesnt work w/ current function b/c it is a int, we need to import a special type "Union"
print(hello(3.14))