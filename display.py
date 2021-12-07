from turtle import Screen
from stage import stage
from cactus import Cactus
from bird import Bird
from vector import Vector
from random import randint

scr = Screen()
scr.title('DINOFLY GAME')
stage = stage(-0.8, 700)

ground_lv = -5
stage.screen_1()
scr.listen()
scr.onclick(stage.click_play)  # click to start game

cac = 500  # amount of cactus
bird = 380  # amount of bird
for i in range(cac):
    # loop to append to stage
    random = randint(500, 1200)
    small_cac = Cactus(Vector(random, ground_lv))
    stage.append(small_cac)

for i in range(bird):
    # loop to append to stage
    random = randint(500, 1200)
    random_y = randint(30, 180)
    small_bird = Bird(Vector(random, random_y))
    stage.append(small_bird)
scr.mainloop()  # make screen on click works
