# from turtle import Turtle,Screen
# timmy = Turtle()
# print(timmy)
# timmy.shape('turtle')
# timmy.color("coral")
# my_screen = Screen()
# timmy.forward(100)
# print(my_screen.canvheight)
# my_screen.exitonclick()

# from prettytable import PrettyTable
# table = PrettyTable()
# print(table)
# table.add_column('Pokemon',['Pikachu','squirtle','charmander'])
# table.add_column('Type',['Electric','water','fire'])
# print(table.align)
# table.align = 'l'
# print(table)


# class User:
#     def __init__(self,user_id,username):
#         self.id = user_id
#         self.username = username
#         self.followers = 0
#         self.following = 0
#
#     def follow(self,user):
#         user.followers += 1
#         self.following += 1
#
# user_1 = User('001', 'Emmanuel')
# user_2 = User('021', 'Emily')
# user_1.follow(user_2)
# print(user_1.followers)
# print(user_2.followers)
# print(user_1.following)
# print(user_2.following)


# class Questions:
#
#     def __init__(self,text,answer):
#         self.text = text
#         self.answer = answer



class Animals:
    def __init__(self):
        self.num_eyes = 2

    def breathe(self):
        print('Inhale Exhale')

class Fish(Animals):
    def __init__(self):
        super().__init__()

    def breathe(self):  # to inherit the breathe method but also add some other attribute(s)
        super().breathe()
        print('Doing this under water')

    def swim(self):
        print('moving in water')

nemo = Fish()
nemo.swim()
nemo.breathe()
print(nemo.num_eyes)





