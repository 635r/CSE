import random

str()
num = random.randint(1, 50)
print(num)
response = ""


while response != num:
    response = input("GuesstheNumber ")
Guess = input('GuesstheNumber')




def compare_number(num):
    if num >= Guess:
        return "lower"
    elif num <= Guess:
        return "higher"