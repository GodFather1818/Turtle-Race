
import turtle as t
import random

is_race_on = False

screen = t.Screen()
screen.setup(width=500, height=400)
colours = ['red', 'orange', 'yellow', 'green', 'blue', 'purple']
all_turtle = []
user_bet = screen.textinput(title='MAKE YOUR BET. ', prompt='WHICH TURTLE WILL WIN THE RACE? ENTER A COLOUR: ').lower()
print(user_bet)
y_position = [-100, -60, -20, 20, 60, 100]
for turtle_index in range(0, 6):
    new_turtle = t.Turtle(shape='turtle')
    new_turtle.color(colours[turtle_index])
    new_turtle.penup()
    # i = 40
    new_turtle.goto(x=-230, y=y_position[turtle_index])
    all_turtle.append(new_turtle)


if user_bet:
    is_race_on = True


while is_race_on:

    for turtle in all_turtle:
        if turtle.xcor() > 230:
            is_race_on = False
            winning_color = turtle.pencolor()
            if winning_color == user_bet:
                print(f"YOU ARE THE WINNER!! THE  {winning_color.upper()} TURTLE has won!")
            else:
                print(f"You have lost! The {winning_color.upper()} TURTLE has won!")
        random_distance = random.randint(0, 10)
        turtle.forward(random_distance)


screen.exitonclick()
