from turtle import Turtle

STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280

class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.penup()
        self.color("deepskyblue3")
        self.speed("fastest")
        self.setheading(90)
        self.goto(STARTING_POSITION)

    def move_turtle(self):
        """
        Description:
            Method to move the turtle by 10 units.
        """
        self.forward(MOVE_DISTANCE)
