from turtle import Screen,Turtle
from snake import Snake
from scoreboard import Scoreboard
from food import Food
from square_game import Square
import time
window=Screen()
def circle():
    mo=Turtle("circle")
    mo.speed("fastest")
    mo.color("navy")
    mo.penup()
    mo.goto(0,-100)
    mo.pendown()
    for _ in range(20):
     mo.circle(100)
     mo.left(360/20)
window.tracer(0) 
my_snake=Snake()
food=Food()
square=Square()
score=Scoreboard()
window.title("Snake game")
window.setup(width=850,height=850)
window.bgcolor("black")
game_on=True
while game_on:
    my_snake.move()
    window.listen()
    
    window.onkey(my_snake.up,"Up")
    window.onkey(my_snake.down,"Down")
    window.onkey(my_snake.right,"Right")
    window.onkey(my_snake.left,"Left")
    square.draw_square()
    window.update()
    time.sleep(0.05)
    if my_snake.head.distance(food)<15:
        #print("Yummy Food ^_^")
        food.appear()
        my_snake.extend()
        score.increase_score()
    if my_snake.head.xcor()>360 or my_snake.head.xcor()<-360 or my_snake.head.ycor()<-360 or my_snake.head.ycor()>360:
        game_on=False
        time.sleep(1)
        window.clear()
        circle()
        time.sleep(1)
        score.game_over()
    if score.score >10:
        my_snake.head.color("red")
        for i in range(len(my_snake.turtles)-1):
            my_snake.turtles[i].color("blue")
    if score.score >20:
        my_snake.head.color("violet")
        for i in range(len(my_snake.turtles)-1):
            my_snake.turtles[i].color("purple")
    if score.score >50:
        my_snake.head.color("aqua")
        for i in range(len(my_snake.turtles)-1):
            my_snake.turtles[i].color("cyan")
    for segment in my_snake.turtles[:-4]:
        if my_snake.head.distance(segment)<10:
            game_on=False
            time.sleep(1)
            window.clear()
            circle()
            time.sleep(1)
            score.game_over()
window.exitonclick()