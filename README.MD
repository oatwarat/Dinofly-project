# DINOFLY GAME 🦕
✰✰✰✰✰✰✰✰✰✰✰✰✰✰✰✰✰✰✰✰✰✰✰✰✰✰✰✰✰✰✰✰✰✰✰✰✰✰✰✰✰✰✰✰✰✰✰✰✰✰✰✰✰
## Overview

This is a game project. The idea of this game is from the dinosaur game in **Google Chrome**. The project is called
`Dinofly` game is because it is different from the actual dinosaur game. This game can fly up into the sky to avoid
the obstacles and earn 5 points each time you have passed through each obstacle.

####❤️ Welcome page

* The welcome page is the welcome screen to the game, in this page there's only one thing you should do which is to 
  click `PLAY` button in the middle of the page. After that, the pop-up button will pop to ask you to write your name
  to continue to the main page and start playing the game.
    
![Welcome page](welcome page.gif)
  
####❤️ Playing

* After done putting the name in welcome page, the `main game-screen` will automatically appear on the screen.
   The job for user to do is to `play(jump)` to avoid those obstacles and **stay alive** as long as possible. While users
   are playing, the users will get 5 scores for each time you passed through the obstacle, but if you hit the obstacles,
   it means you are dead(game over). The obstacles in here will be coming **faster** when you reach certain points. 
   In ex. when you started the game the obstacles start with the speed of 4, but when you achieved 50 points the 
   obstacle's speed might be 7
  
![This is a second page](playing page.gif)


####❤️ Game over

* After you hit the obstacles, playing screen will automatically disappear and this screen(game over) will be appearing
  after that. In this screen it will show you how many scores you have earned, what's current high score right now
  and done by whom.
  
 


![This is a second page](game ov.gif)

### Required

*  `turtle`, `Turtle`, `random`, `screen`, and `json`

### Program design

* __7 classes__

1. class `Vector` is a class to help set position of other classes(other turtles)


2. class `Dinosaur` is a class where we create the actual dinosaur which I imported the image of the dinosaur and 
   make the dinosaur jump which is `dinofly`. Nevertheless, I also put the __gravity__ so that when the dinosaur jumps it
   will fall down slowly.
   

3. class `Bird` has a duty to store coordinate which is __position__ and render the shape.


4. class `Cactus` has a duty to store coordinate which is __position__ and render the shape.


5. class `Interface` mostly create the turtles and texts that will appear in main screen.


6. class `Stage` is the most important class because it is the class where all the __classes__ and __attributes__ are
   combined and gather to make the gameplay. In this class, we store the score, create the screen, json file, and make
   the turtle runs.


7. class `Display` is where the user will run this program. In this class, we import the previous class which is stage
  and in this class we make the code becomes short and understandable. Furthermore, in this class I use this class
  to make the obstacles in for-loop to append those objects into __list of objects__ in stage.
      
* The program must be run in display.py by the user.

### Code structure


* There are one type of files that are used: json
    - `users.json` used to keep track of the user's name and user's score.