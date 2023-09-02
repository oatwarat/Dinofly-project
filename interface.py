from turtle import Turtle
import turtle

screen = turtle.Screen()


class Interface:
    def __init__(self):
        # creating all the turtles, these turtles are the texts and pictures.
        self.draw = Turtle()
        self.draw_1 = Turtle()
        self.play = Turtle()
        self.over = Turtle()
        self.text = Turtle()
        self.sun = Turtle()
        self.space = Turtle()

    def start(self):
        # this method is the welcome screen to the users which contain texts and picture.
        screen.addshape('pictures/background.gif')
        self.draw.shape("pictures/background.gif")
        self.play.color('goldenrod3')
        self.play.speed(0)
        self.play.hideturtle()
        self.play.color('LavenderBlush4')
        self.play.penup()
        self.play.goto(-120, 75)
        self.play.pendown()
        self.play.write("Play🦕", font=("Calibre", 55, "bold"))
        self.play.hideturtle()
        self.play.color('white')
        self.play.penup()
        self.play.goto(-215, -320)
        self.play.pendown()
        self.play.write("Welcome to Dinofly!", font=("Calibre", 35, "bold"))

    def after_int(self):
        # this is the picture that will appear in the gaming phase.
        screen.addshape('pictures/playing.gif')
        self.draw_1.shape("pictures/playing.gif")

    def game_over(self):
        # this is the picture that will appear after you lose.
        screen.addshape('pictures/game_over.gif')
        self.over.shape("pictures/game_over.gif")

    def txt(self):
        # this is the text after game over and it will tell you to click to exit.
        self.text.color('light pink')
        self.text.speed(0)
        self.text.penup()
        self.text.goto(-120, -300)
        self.text.pendown()
        self.text.write('click anywhere to exit :D', font=("Calibre", 15, "bold"))

    def sunlight(self):
        # this is the a sun picture of the sun in playing phase.
        self.sun.speed(0)
        self.sun.hideturtle()
        screen.addshape('pictures/sun.gif')
        self.sun.shape("pictures/sun.gif")
        self.sun.penup()
        self.sun.goto(140, 265)
        self.sun.showturtle()

    def space_bar(self):
        # this is the text that says 'press space to jump'
        self.space.speed(0)
        self.space.color('white')
        self.space.hideturtle()
        self.space.penup()
        self.space.goto(-115, -315)
        self.space.write('press space_bar to jump ^^', font=("Calibre", 12, "bold"))
        self.space.showturtle()
