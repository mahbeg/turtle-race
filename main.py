from turtle import Turtle, Screen
import random


is_race_on = False
colors = ["red", "blue", "green", "yellow", "purple", "pink"]
speed = [0, 10, 6, 3, 1]
poses = [-100, -50, 0, 50, 100, 150]

screen = Screen()
screen.colormode(255)
screen.setup(width=500, height=400)
user_bet = screen.textinput("turtle race", "which do you choose: ")

all_turtle = []
for turtle_index in range(0, 6):
    tim = Turtle(shape="turtle")
    tim.penup()
    tim.color(colors[turtle_index])
    tim.goto(-230, poses[turtle_index])
    all_turtle.append(tim)

# print(all_turtle)


if user_bet:
    is_race_on = True




while is_race_on == True:
    for item in all_turtle:
        if item.xcor() < 230:
            distance = random.randint(0,10)
            item.forward(distance)
            if item.xcor() == 230:
                winner = item.color()
                is_race_on = False
                if winner == user_bet:
                    print(f"you win, winner turtle is {winner}")
                else:
                    print(f"you lost, winner turtle is {winner}")











screen.exitonclick()