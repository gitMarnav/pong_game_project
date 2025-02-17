from turtle import Turtle
PADDLE_SHAPE = 'square'
PADDLE_COLOR = 'gray10'


class Paddle(Turtle):
    def __init__(self, x_coordinate, y_coordinate):
        super().__init__()
        self.shape(PADDLE_SHAPE)
        self.color(PADDLE_COLOR)
        self.shapesize(stretch_len=1, stretch_wid=5)
        self.set_position(x_coordinate, y_coordinate)

    def set_position(self, x_coordinate, y_coordinate):
        self.up()
        self.goto(x_coordinate, y_coordinate)

    def go_up(self):
        new_coord = self.ycor() + 20
        self.sety(new_coord)

    def go_down(self):
        new_coord = self.ycor() - 20
        self.sety(new_coord)
