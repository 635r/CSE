# # # Defining a Class
# # class Cat(object):
# #     # TWO UNDERSCORES BEFORE AND AFTER
# #     def __init__(self, color, personality, pattern):
# #         # THINGS THAT A CAT HAS
# #         self.color = color
# #         self.personality = personality
# #         self.pattern = pattern
# #         self.state = "happy"
# #         self.hungry = False
# #
# #
# # # THINGS THAT CATS CAN DO :
# #     def jump(self):
# #         self.state = "Scared"
# #         print("the cat jumps")
# #
# #     def play(self):
# #         self.state = "happy"
# #         print("you play with the cat")
# #
# #
# # # (Instantiating) two cats
# # cute_cat = Cat("brown", False,"spots")
# # cute_cat2 = Cat("grey", False, "no spots")
# #
# #
# #  #getting info about the cats
# # print(cute_cat.color)
# # print(cute_cat2.state)
# # print(cute_cat2.color)
# #
# # cute_cat.jump()
# # print(cute_cat.state)
# # print(cute_cat2.state)
# #
# # cute_cat.play()
# # print(cute_cat.state)
#
#
# class Car(object):
#     def __init__(self, color, brand, num_of_cylinder):
#         self.color = color
#         self.brand = brand
#         self.num_of_cylinder = num_of_cylinder
#         self.engineOn = False
#
#     def turn_on(self):
#         if self.engineOn:
#             print("Nothing Happens")
#             self.engineOn = True
#
#     def move_forward(self):`1
#         if self.engineOn:
#             print("you move forward")
#         else:
#             print("Nothing Happened")
#
#     def turnOff(self):
#         if self.engineOn:
#             self.engineOff
#
# my_car = Car(4, "Subaru", "Blue")
#
# my_car.turn.on()
# my_car.move_forward()
# my_car.turn_off()
