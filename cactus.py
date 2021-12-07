import turtle


screen = turtle.Screen()


class Cactus:

    def __init__(self, pos):
        # the initial part is to store the position
        """

        :param pos: int
        """
        self.pos = pos
        self.a = 0

    def render(self, cactus):
        # this function is to create the shape and looks of the cactus
        """

        :param cactus: Turtle
        """
        cactus.penup()
        cactus.speed(0)
        cactus.goto(self.pos.x, self.pos.y)
        cactus.pendown()
        screen.addshape('cactus.gif')
        cactus.shape("cactus.gif")
        cactus.shapesize(1)
        cactus.height = 150
        cactus.width = 150
        cactus.color("green")
