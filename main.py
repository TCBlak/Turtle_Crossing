import time
from turtle import Screen
from player import Player, FINISH_LINE_Y
from car_manager import CarManager
from scoreboard import Scoreboard
import random

screen = Screen()
screen.setup(width=600, height=600)
screen.bgpic('graphics/highway_lanes.png')
screen.tracer(False) # Turns off automatic screen update.
screen.title('Turtle Crossing - Definitely NOT Frogger')

player = Player()
scoreboard = Scoreboard()
car_manager = CarManager()

car_manager.create_car()

screen.listen()
screen.onkey(fun=player.move, key='Up')

game_is_on = True
# The game loop
while game_is_on:
    time.sleep(scoreboard.delay)
    # update the cars to move them
    car_manager.update_cars()
    # check if turtle has made it across
    if player.ycor() >= FINISH_LINE_Y:
        scoreboard.update_level()
        player.reset_player()
    # check to see if we need to add another car
    if random.random() < scoreboard.car_prob:
        car_manager.create_car()
    # check for collision with car
    if car_manager.is_collision(player):
        scoreboard.game_over()
        game_is_on = False

    screen.update()

screen.exitonclick()
