from turtle import Turtle

class Paddle(Turtle):

    def __init__(self, position):
        super().__init__()
        self.shape('square')
        self.color('black')
        self.shapesize(stretch_wid=0.5, stretch_len=4)
        self.penup()
        self.setposition(position)

    def move_left(self):
        new_x =self.xcor()-10
        self.goto(new_x, self.ycor())

    def move_right(self):
        new_x = self.xcor()+10
        self.goto(new_x, self.ycor())



