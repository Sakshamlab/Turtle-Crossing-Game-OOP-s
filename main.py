import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)
player = Player()
screen.listen()
screen.onkey(fun=player.move, key="Up")
cars = CarManager()
score = Scoreboard()
game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()
    cars.randomcars()
    cars.move_cars()

    for car in cars.all_car:
        if car.distance(player) < 18 :
            score.gameover()
            game_is_on = False

    if player.is_at_finishline():
        player.goto_start()
        cars.next_level()
        score.addscore()





screen.exitonclick()



