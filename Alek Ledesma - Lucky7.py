#Alek Ledesma PERIOD 7  1/16/18
import random

num_rolls = 0

money_left = 15

high_point = 0

max_money = 0


while money_left > 0:

    die = random.randint(1, 6)

    dice = random.randint(1, 6)

    num = die + dice

    if num == 7:
        print("NOICE")
        money_left += 4
        num_rolls += 1
        print("you have %s buck(s)" % money_left)

        if max_money < money_left:
            max_money = money_left
            high_point = num_rolls

    elif num != 7:
        print("oof")
        money_left -= 1
        num_rolls += 1
        print("you have %s buck(s) left" % money_left)

if money_left is 0:

    print("you rolled %s times" % num_rolls)

    print("Gambling is a sin")

    print("You should have stopped at round %s" % high_point)

    print("while you had %s bucks" % max_money)
