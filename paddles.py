from turtle import Turtle

class Paddle(Turtle):
    def __init__(self,position):
        super().__init__()
        self.shape("square")
        self.color("white")
        self.shapesize(4,1)
        self.penup()
        self.goto(position)


        #controlling paddles now
    def move_up(self):
        new_y=self.ycor()+20
        self.goto(self.xcor(),new_y)

    def move_down(self):
        new_y=self.ycor()-20
        self.goto(self.xcor(),new_y)