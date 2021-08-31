"""Exercise 01 program 3 relational_operators 10 pts."""

__author__ = "730330989"

left: str = (input("Left-hand side: "))
right: str = (input("Right-hand side: "))
left_num: int = int(str(left))
right_num: int = int(str(right))
print(left + " < " + right + " is " + str(bool(left_num < right_num)))
print(left + " >= " + right + " is " + str(bool(left_num >= right_num)))
print(left + " == " + right + " is " + str(bool(left_num == right_num)))
print(left + " != " + right + " is " + str(bool(left_num != right_num)))