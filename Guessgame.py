# Type Guess Beneath
guess = 24

import random
print(random.randint(0, 50))

num = random


def guess_num(num):
    if num >= guess:
        return "lower"
    elif num <= guess:
        return "higher"
