from turtle import Turtle, Screen

ground_lv = -115
gravity = -0.8
screen = Screen()


class Dinosaur:
    def __init__(self, pos):
        # in this initial function is to create a turtle(dinosaur) and store position
        """

        :param pos: int
        """
        self.dina = Turtle()
        self.pos = pos
        self.dy = 0

    def lil_dino(self):
        # this function is to create a dinosaur shape and ask to go to position where we want
        self.dina.hideturtle()
        self.dina.left(90)
        screen.addshape('pictures/dinofly.gif')
        self.dina.shape("pictures/dinofly.gif")
        self.dina.shapesize(1)
        self.dina.height = 200
        self.dina.width = 200
        self.dina.color("green")
        self.dina.penup()
        self.dina.goto(self.pos.x, self.pos.y)
        self.dina.showturtle()

    def update(self):
        # this is the function that set y-cor of dinosaur when it jumps, the y-cor of dinosaur will +14
        self.dy = 14
        print('jumping 🦕!')

    def gravity(self):
        # this function is set to have the gravity like the real world so when you jump it will fall down
        # like the gravity in real life and set the ground and the ceiling of the screen so our dinosaur
        # won't go out of the screen we set.
        self.dy += gravity
        y = self.dina.ycor()
        y += self.dy
        self.dina.sety(y)
        if self.dina.ycor() < ground_lv + self.dina.height/2:
            self.dina.sety(ground_lv + self.dina.height/2)
            self.dy = 2
        if self.dina.ycor() > (500 - 200 / 2) - 70:
            self.dina.sety(280)
            self.dy = 1
        screen.update()
