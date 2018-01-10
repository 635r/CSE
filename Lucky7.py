import random

num_rolls = 0


money_left = 15

while money_left > 0:

    die = random.randint(1, 6)

    dice = random.randint(1, 6)

    num = die + dice

    high_point = 0

    if num == 7:
        print("NOICE")
        money_left += 4
        num_rolls += 1
        print("you have %s buck(s)" % money_left)

    elif num != 7:
        print("oof")
        money_left -= 1
        num_rolls += 1
        print("you have %s buck(s) left" % money_left)

if money_left is 0:
    
    print("Gambling is a sin")
    print("you rolled %s times" % num_rolls)
    print("you should have stopped at %s" % high_point)
