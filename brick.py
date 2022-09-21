from turtle import Turtle

class Brick(Turtle):

    def __init__(self, position):
        super().__init__()
        self.shape('square')
        self.color('black')
        self.shapesize(stretch_wid=1, stretch_len=2)
        self.penup()
        self.setpos(position)

    def destroy(self):
        self.destroy()