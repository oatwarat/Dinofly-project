from turtle import Turtle, Screen
from dinosaur import Dinosaur
from vector import Vector
from random import shuffle
from interface import Interface
import json


class stage:

    def __init__(self, gravity, max_lv):
        # this initial is to create the turtles, list of objects, and import the dinosaur and interface class
        """

        :param gravity: int
        :param max_lv: int
        """
        self.screen = Screen()
        self.obs = Turtle()
        self.app = Turtle()
        self.done = Turtle()
        self.show = Turtle()
        self.dinosaur = Dinosaur(Vector(-420, -45))  # set initial position of dinosaur
        self.int = Interface()
        self.name = ''
        self.obstacles = []  # list of objects
        self.high = []
        self.gravity = gravity
        self.max_lv = max_lv
        self.scores = 0

    def update_dinosaur(self):
        # this function is to update the position of dinosaur when it jumps and gravity.
        self.dinosaur.gravity()
        self.screen.cv.after(ms=1, func=self.update_dinosaur)

    def click_play(self, x, y):
        # this function is quite the overall that are important in hereto ask user to click play then it will show up
        # all the turtles that I input in and begin the game. I also set the onkey press in here so it will run
        # continually.
        """

        :param x: int
        :param y: int
        """
        if -155 < x > -165 and 60 < y > 50:
            self.name = self.screen.textinput("enter ur name :D", "type here!!")
            self.screen.clear()
            self.int.after_int()
            self.dino()
            self.int.sunlight()
            self.int.space_bar()
            self.screen.listen()
            self.screen.onkeypress(self.jump, 'space')
            self.screen.update()
            self.screen.cv.after(ms=1, func=self.update_dinosaur)
            self.render()
            self.screen.exitonclick()

    def screen_1(self):
        # this is screen no.1 that set the interface of the game
        self.screen.setup(1000, 700)
        self.int.start()

    def screen_2(self):
        # this is just to set the size of the screen 2
        self.screen.setup(1000, 700)

    def dino(self):
        # this function is to call the dinosaur
        self.dinosaur.lil_dino()
        self.dinosaur.height = 200
        self.dinosaur.width = 200

    def jump(self):
        # this one is to call the update function from dinosaur
        self.dinosaur.update()

    def append(self, obs):
        # this one is linked with the display page that will append stuff in display page to the list in here.
        """

        :param obs: object
        """
        self.obstacles.append(obs)

    def random_obstacles(self):
        # random function is to shuffle the position in the list so when it comes out it will randomly arrange.
        shuffle(self.obstacles)

    def render(self):
        # this render function is to set the speed of the obstacles of each stage and set the obstacles to move
        # in the for loop and while for loop runs the scores will count after each obstacles had passed, but if it hit
        # the game will automatically stops.

        self.random_obstacles()
        self.obs.clear()
        for i in range(len(self.obstacles)):
            self.obstacles[i].render(self.obs)
            self.obs.penup()
            self.obs.speed(6)
            if 0 <= self.scores >= 10:
                self.obs.speed(6)
            if 15 <= self.scores >= 25:
                self.obs.speed(7)
            if 30 <= self.scores >= 45:
                self.obs.speed(8)
            if 50 <= self.scores >= 70:
                self.obs.speed(9)
            if 70 <= self.scores >= 95:
                self.obs.speed(10)
            if self.scores > 100:
                self.obs.speed(10)
            self.obs.showturtle()
            self.obs.goto(-355, self.obstacles[i].pos.y)
            self.obs.hideturtle()
            self.score()
            self.render_score()
            if self.obstacles[i].pos.y - 65 < self.dinosaur.dina.ycor() < self.obstacles[i].pos.y + 65:
                self.scores -= 5
                break

        self.save_score()
        self.screen.clear()
        self.int.game_over()
        self.show_score()

    def show_score(self):
        # show score function is to write the texts that show the score that user in that round got and the
        # overall high score and name
        self.high_score()
        self.show.color('LavenderBlush1')
        self.show.speed(0)
        self.show.hideturtle()
        self.show.penup()
        self.show.goto(-135, -80)
        self.show.pendown()
        self.show.write(f'{self.name} scores: {self.scores}', font=("Calibre", 30, "bold"))
        self.show.penup()
        self.show.goto(-105, -120)
        self.show.pendown()
        self.show.write(f'Highest score: {self.high[-1][0]}', font=("Calibre", 18, "bold"))
        self.int.txt()
        self.show.penup()
        self.show.goto(-55, -160)
        self.show.pendown()
        self.show.write(f'by: {self.high[-1][1]}', font=("Calibre", 18, "bold"))

    def score(self):
        # score function is to +5 in everytime you passed obstacles.
        self.scores += 5

    def render_score(self):
        # this render_score is set ot appear the current score of user.
        self.app.speed(0)
        self.app.clear()
        self.app.hideturtle()
        self.app.color('LightGoldenRodYellow')
        self.app.penup()
        self.app.goto(400, 270)
        self.app.pendown()
        self.app.write(self.scores, font=("Calibre", 35, "bold"))

    def save_score(self):
        # in this function is to create the json file everytime user play.
        new_data = {self.name: {'name': self.name,
                                'score': self.scores}}
        try:
            with open("users.json", "r") as data_file:
                data = json.load(data_file)
        except FileNotFoundError:
            with open("users.json", "w") as data_file:
                json.dump(new_data, data_file, indent=4)
        else:
            data.update(new_data)
            with open("users.json", "w") as data_file:
                json.dump(data, data_file, indent=4)

    def high_score(self):
        # in this last function is to set the high score of overall json file.
        try:
            with open("users.json", "r") as data_file:
                data = json.load(data_file)
        except FileNotFoundError:
            pass
        else:
            for user in data:
                self.high.append((data[user]['score'], data[user]['name']))
            self.high.sort()
