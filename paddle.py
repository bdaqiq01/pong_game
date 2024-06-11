from turtle import Turtle, register_shape

class Paddle(Turtle):
    def __init__(self, xpos=0):
        super().__init__()
        #paddle_shape = ((0, 0), (0, 20), (100, 20), (100, 0))
        # registering the new shape
        #register_shape("paddle", paddle_shape)

        self.shape("square")
        self.shapesize( stretch_len=1, stretch_wid=5)
        self.color("white")
        self.penup()
        self.goto(x=xpos, y=0)
        self.speed("fastest")

    def up(self):
        new_y = self.ycor() + 50
        self.goto(self.xcor(), new_y)

    def down(self):
        new_y = self.ycor() - 50
        self.goto(self.xcor(), new_y)


