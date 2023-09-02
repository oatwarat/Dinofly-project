import turtle
from random import randint

screen = turtle.Screen()


class Bird:
    random_x = randint(-200, 1000)
    random_y = randint(100, 200)

    def __init__(self, pos):
        # the initial part is to store the position
        """

        :param pos: int
        """
        self.pos = pos

    def render(self, bird):
        # this function is to create the shape and looks of the bird
        """

        :param bird: Turtle
        """
        bird.penup()
        bird.speed(0)
        bird.goto(self.pos.x + self.random_x, self.pos.y + self.random_y)
        bird.pendown()
        screen.addshape('pictures/bird.gif')
        bird.shape("pictures/bird.gif")
        bird.shapesize(1)
        bird.height = 150
        bird.width = 150
        bird.color("green")
