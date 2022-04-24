from turtle import Turtle


class Paddle(Turtle):
    def __init__(self, position):
        super(Paddle, self).__init__()
        self.color("white")
        self.shapesize(stretch_wid=.6, stretch_len=6, outline=0)
        self.shape("square")
        self.penup()
        self.speed("fastest")
        self.goto(position)

    def move_left(self):
        ycor = self.ycor()
        new_xposition = (self.xcor()) - 40
        self.goto(new_xposition, ycor)

    def move_right(self):
        ycor = self.ycor()
        new_xposition = (self.xcor()) + 40
        self.goto(new_xposition, ycor)


class Obstacles(Turtle):
    def __init__(self, position):
        super(Obstacles, self).__init__()
        self.color("green")
        self.shapesize(stretch_wid=1, stretch_len=4, outline=0)
        self.shape("square")
        self.penup()
        self.speed("slow")
        self.goto(position)

    def move_down(self):
        xcor = self.xcor()
        new_yposition = (self.ycor()) - .06
        if self.ycor() < 200:
            self.color('yellow')
        if self.ycor() < 0:
            self.color('red')
        self.goto(xcor, new_yposition)

    def destroy(self):
        self.hideturtle()

