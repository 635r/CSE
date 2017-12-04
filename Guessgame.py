# Type Guess Beneath
import random
print(random.randint(0, 50))

num = random


guess = 24


def guess_num(num):
    if num >= guess:
        return "lower"
    elif num <= guess:
        return "higher"

def tries