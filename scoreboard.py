from turtle import Turtle

class Scoreboard(Turtle):
    
    def __init__(self):
        super().__init__()
        self.penup()
        self.ht()
        self.goto(0,220)
        self.color('black')
        self.write('Score: 0', font=('Arial', 20, 'bold'), align='center')
        self.points = 0

    def score(self):
        self.clear()
        self.points += 1
        self.write(f'Score: {self.points}', font=('Arial', 20, 'bold'), align='center')