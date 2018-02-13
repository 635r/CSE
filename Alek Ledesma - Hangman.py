import random

guess_left = 10

word_bank = ["bamboozle", "python", "think", "perplex", "confuse", "challenge", "ironically", "thanks", "hello"]

word = random.choice(word_bank)

word_bank.remove(word)

print(guess_left)

letters_guessed = []

while guess_left > 0:

    response = input("guess here.")
    letters_guessed.append(response)
    output = []

    if response == word:
        print("you are indeed correct, now type the letters in one at a time")

    if response not in word:
            guess_left -= 1

    else:
        for letter in word:
            if letter in letters_guessed:
                output.append(letter)

            else:
                    output.append("*")
            if str1 == word:
                print("you win")
                quit()

    str1 = "".join(output)
    print(str1)
    print(guess_left)
    print(letters_guessed)
    if guess_left == 0:
        print("hey stop loosing")
        print("the word was %s" % word)
        quit()

print("after you guess all the letters, press enter again")

# Outline of hangman
# 1. Make a word bank - 10 items
# 2. select a random item from the list
# 3. add in user input into guessed words
# 4. hide the word (use stars)
# 5. reveal letters if they have been guessed
# 6. create the win condition
