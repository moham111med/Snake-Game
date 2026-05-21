from turtle import Turtle
class Snake:
    def __init__(self):
        self.turtles=[]
        self.position=[(-40,0),(-20,0),(0,0),(20,0),(40,0),(60,0)]
        self.creat_snake()
        self.head=self.turtles[-1]
    def creat_snake(self):
      for i in range(len(self.position)): 
        new_turtle=Turtle(shape="square")
        new_turtle.penup()
        new_turtle.color("white")
        new_turtle.goto(self.position[i])
        self.turtles.append(new_turtle)
      # self.turtles[-1].shape("circle")
      self.turtles[-1].color("cyan")
      #  self.turtles[0].shape("triangle")
    def move(self):
        for i in range(len(self.turtles)-1):
          self.turtles[i].goto(self.turtles[i+1].pos())
        self.head.forward(10)
      #  self.turtles[0].setheading(0)
    def extend(self):
       new_segment=Turtle("square")
       new_segment.color("white")
       new_segment.penup()
       new_segment.goto(self.turtles[0].pos())
       self.turtles.insert(0,new_segment)
    def up(self):
       self.head.setheading(90)
      #  self.turtles[0].setheading(270)
    def down(self):
       self.head.setheading(-90)
      #  self.turtles[0].setheading(90)
    def right(self):
       self.head.setheading(0)
       #self.turtles[0].setheading(180)
    def left(self):
       self.head.setheading(180)