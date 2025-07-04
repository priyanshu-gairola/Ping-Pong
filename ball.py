from turtle import Turtle



class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.movx=10
        self.movy=10
        self.speed = 0.1
        self.shape("circle")
        self.color("white")
        self.penup()



    def move_ball(self):
        new_x=self.xcor()+self.movx
        new_y = self.ycor() + self.movy
        self.goto(new_x,new_y)

    def bounce_y(self):  #when reaches top and bottopm side
        self.movy*=-1

    def bounce_x(self):  #when cillides with paddles
        self.movx *=-1

    def restart(self):
        self.goto(0,0)
        self.speed=0.1
        self.bounce_x()

    #increase ball speed after bouncing from paddles
    def incr_speed(self):
        self.speed *= 0.8

