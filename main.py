from turtle import Turtle, Screen
import random

my_screen = Screen()
my_screen.setup(width=500,height=400)
user_choice = my_screen.textinput("Turtle Betting!", "Welcome to the turtle race! \nTo start, bet on either red, orange, yellow, green, blue, purple and see if they win!").lower()
print(f"Great! You chose the {user_choice} turtle")
race_on = False

colors = ["red","orange","yellow","green","blue","purple"]
race_turtles = []


y_coordinate = 100
for i in range(6):
    new_turtle=Turtle(shape="turtle")
    new_turtle.color(colors[i])
    new_turtle.pu()
    new_turtle.goto(-230, y_coordinate)
    y_coordinate -= 40
    race_turtles.append(new_turtle)

if user_choice:
    race_on = True

while race_on:
    for turtles in race_turtles:
        if turtles.xcor() >= 230:
            winning_turtle = turtles
            race_on = False
            if user_choice == winning_turtle.pencolor():
                print(f"You win! The winning turtle is the {winning_turtle.pencolor()} turtle.")
            else:
                print(f"You lost! The winning turtle is the {winning_turtle.pencolor()} turtle.")
        distance = random.randint(5,15)
        turtles.fd(distance)
    




my_screen.exitonclick()