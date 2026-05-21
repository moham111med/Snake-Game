from turtle import Turtle
class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score=0
        self.penup()
        self.highscore=self.get_highscore()
        self.color("white")
        self.goto(0,390)
        self.hideturtle()
        self.update_scoreboard()
    def update_scoreboard(self):
        self.write(f"Score: {self.score}\tHigh score: {self.highscore}",align="center",font=("arial",24,"normal"))
    def increase_score(self):
        self.score+=1
        self.clear()
        self.update_scoreboard()
    def game_over(self):
        self.clear()
        if self.score>self.highscore:
            self.highscore=self.score
            with open('database.txt','w') as f:
                f.write(str(self.highscore))   
            self.get_highscore()
        self.screen.bgcolor("yellow")
        self.goto(0,150)
        self.color("green")
        self.write(f"{'-'*20}Game Over{'-'*20}\n\n{' '*20}Final Score: {self.score}\n\n{' '*20}High Score: {self.highscore}",align="center",font=("arial",45,"normal"))
    def get_highscore(self):
        with open('database.txt','r') as file:
            file.seek(0)
            score_number=int(file.read())
            return score_number
    