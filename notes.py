# print("hello world")
#
# # Alek Ledesma
#
# # ctrl+/ to toggle between comments
#
# print(3+12)
# print(3**3)
#
# print("see if you can figure this out")
# print(13 % 12)
# print(5 % 3)
# print(103 % 100)
#
# # Variables
# car_name = 'Weibe Mobile'
# car_type = 'lambroghini sesto elemento'
# car_cylinder = 8
# car_mpg = 9000.1
#
# # Inline Printing
# print('my car is the %s. It is a %s' % (car_name, car_type))
#
# # Taking Input
# name = input('The big bamboozle')
# print('Hello %s.' % name)
# age = input("14")
# print("wow %s " % age)
#
# # Change file
#
#
# def print_hw():
#     print("Hello World")
#
#
# print_hw()
#
#
# def say_hi(name):
#     print("Hello %s." % name)
#     print("I hope you have a fantastic day.")
#
#
# say_hi("The Big Bamboozle")
#
#
# def birthday(age):
#     age += 1
#
#
# # age=age+1
#
#
# say_hi("The Big Bamboozle")
# print("The Big Bamboozle is 14. Next year he'll be 15")
#
# birthday(15)
# # CTRL+A =select all
#
#
# def f(x):
#     return x ** 5 + 4 * x ** 4 - 17 * x ** 2 + 4
#
#
# print(f(3))
#
#
# print(f(3) + f(5))
#
#
# # If Statements
#
#
# def grade_cal(percentage):
#     if percentage >= 90:
#         return "A"
#     elif percentage >= 80:
#         return "B"
#     elif percentage >= 70:
#         return "C"
#     elif percentage >= 60:
#         return "D"
#     elif percentage <= 60:
#         return "F"
#
# # Loops
# # for num in range(5):
# #     print(num + 1)
#
#
# for bamboozle in "Hello World":
#
#     print(bamboozle)
# a = 1
# while a < 10:
#     print(a)
#     a += 1
# response = ""
# while response != "Hello":
#     response = input("Say \"Hello\"")
#
# print("Hello \nWorld")
#
# # n\ means new line
#
# import random
# print(random.randint(0, 6))
#
#
# #two equal sings to compare
# print(1 == 1)
#
# print(1 != 2)
# print(not False)
# print(1 == 1 and 4 <= 5)
# print(1 < 0 or 5> 1)
#
#
# c = "1"
# print(c == 1)       # False since C is a string and
#
# print (int(c) == 1)
#
# print(c == str(1))

the_count = [1,2,3,4,5]
characters = ['graves', 'dory', 'boots', 'dora', 'shrek', 'obi-wan', 'Chin Chin']
print(characters[4])

print(len(characters))   #Gives length of list

for char in characters:
    print(char)

for num in the_count:
    print(num ** 2)

len(characters)
range(3)    #makes a list of numbers from 0 to 2

range(len(characters))  #makes a list of ALL INDICIES

for num in range(len(characters)):
    char = characters[num]
    print("the character at index%d is %s" % (num, char))

str1 = "HELLO WORLD!"
listOne = list(str1)
print(listOne)
listOne[11] = '.'
newStr = ''.join(listOne)
print(newStr)

print(listOne[-2])

# adding to a list
characters.append('batman')
characters.append('Francis of the Filth')
print(characters)


#removing characters from a list
characters.remove("shrek")
print(characters)

#string class
import string
print(string.ascii_letters)
print(string.ascii_lowercase)
print(string.digits)
print(string.punctuation)

strTwo = 'WHAt iF tHe hATErs dAb BAck?...'
lowercase = strTwo.lower()
print(lowercase)
