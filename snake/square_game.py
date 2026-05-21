from turtle import Turtle
class Square(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.color("red")
        self.penup()
    def draw_square(self):
        self.goto(380,-380)
        self.pendown()
        self.pensize(10)
        for _ in range(4):
            self.left(90)
            self.fd(760)