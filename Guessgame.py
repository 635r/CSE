import random

number = random.randint(1, 50)

right_guess = False

turns_left = 5


while turns_left > 0 and right_guess is False:
    answer = int(input("try and guess"))
    if answer == number:
        print("NOICE")
        right_guess = True
    elif answer > number:
        print("lower m9")
        turns_left -= 1
    elif answer < number:
        print("higher m8")
        turns_left -= 1


if turns_left is 0:
    print("sory you got hecked. This was the number %s." % number)
