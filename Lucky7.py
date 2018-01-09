#B E G O N E T H O T
import random

die = random.randint(1, 6)

dice = random.randint(1, 6)

num = die + dice

money_left = 15

while money_left > 0:
    if num == 7:
        print("NOICE")
        money_left += 4
    elif num > 7:
        print("lower m9")
        money_left -= 1
    elif num < 7:
        print("higher m8")
        money_left -= 1


if money_left is 0:
    print("sory you got hecked.")

