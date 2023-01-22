
from turtle import Screen
from car import Car
import random
from player import Player
import time
from score_board import ScoreBoard

screen = Screen()
screen.setup(width=400, height=600)

screen.tracer(0)

player = Player()
car = Car()
score_board = ScoreBoard()

screen.listen()
screen.onkey(player.move_up, "Up")

game_is_on = True

while game_is_on:
    screen.update()

    car.create_car()
    car.move_cars()


    for c in car.all_cars:
        if c.xcor() < 10 and c.distance(player) < 20:
            score_board.game_over()
            game_is_on = False

    if player.is_at_finish_line():
        player.go_to_start()
        car.level_up()
        score_board.update_score()

    time.sleep(0.1)



screen.exitonclick()