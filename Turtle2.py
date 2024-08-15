# from turtle import Turtle, Screen
# tim = Turtle()
# screen = Screen()
#
# def move_forwards():
#     tim.forward(10)
#
# def move_backwards():
#     tim.backward(10)
#
# def turn_left():
#     tim.left(10)
#
# def turn_right():
#     tim.right(10)
#
# def clear():
#     tim.clear()
#     tim.penup()
#     tim.home()
#     tim.pendown()
#
# screen.listen()
# screen.onkey(move_forwards, 'd')
# screen.onkey(move_backwards, 'a')
# screen.onkey(turn_left, 'w')
# screen.onkey(turn_right, 's')
# screen.onkey(clear, 'c')
# screen.exitonclick()



from turtle import Turtle, Screen
from  random import randint
screen = Screen()
is_race_on = False
screen.setup(width=500, height=400)
screen.title('TURTLE RACING GAME')
screen.listen()
userbet=screen.textinput(title='Make your bet', prompt='Which turtle will win the race'
                                                       ' ? Enter a color').lower()
colors = ['red', 'blue', 'orange', 'purple', 'yellow','green']
y_positions = [-100,-60,-20,20,60,100]
all_turtles = []

for turtle_index in range(0,6):
    new_turtle = Turtle(shape='turtle')
    new_turtle.penup()
    new_turtle.color(colors[turtle_index])
    new_turtle.goto(x=-240, y=y_positions[turtle_index])
    all_turtles.append(new_turtle)

if userbet:
    is_race_on = True
while is_race_on:
    for turtle in all_turtles:
        if turtle.xcor() > 215:
            is_race_on = False
            winning_color = turtle.pencolor()
            if winning_color == userbet:
                print(f'You Won!. The {winning_color} turtle is the winner')
            else:
                print(f'You lose!. The {winning_color} turtle is the winner')
        rand_range = randint(3,9)
        turtle.forward(rand_range)

screen.exitonclick()
