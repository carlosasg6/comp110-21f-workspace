"""Exercise 01 program 2 numeric_operators 25 pts."""

__author__ = "730330989"

left: str = (input("Left-hand side: "))
right: str = (input("Right-hand side: "))
left_num: int = int(str(left))
right_num: int = int(str(right))
ans_1: str = str(int(left_num ** right_num))
ans_2: str = str(float(left_num / right_num))
ans_3: str = str(int(left_num // right_num))
ans_4: str = str(int(left_num % right_num))
print(left + " ** " + right + " is " + ans_1)
print(left + " / " + right + " is " + ans_2)
print(left + " // " + right + " is " + ans_3)
print(left + " % " + right + " is " + ans_4)