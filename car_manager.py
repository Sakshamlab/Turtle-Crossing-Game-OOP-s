from turtle import Turtle

from random import randint, choice
COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManager():
    def __init__(self):
        self.all_car = []
        self.car_speed = STARTING_MOVE_DISTANCE

    def randomcars(self):
        randomnumber = randint(1,6)
        if randomnumber == 1:
            cars = Turtle()
            cars.shape("square")
            cars.color(choice(COLORS))
            cars.penup()
            cars.shapesize(stretch_wid=1, stretch_len=2)
            new_y = randint(-250, 250)
            cars.goto(x=300, y=new_y)
            self.all_car.append(cars)

    def move_cars(self):
        for cars in self.all_car:
            cars.backward(self.car_speed)

    def next_level(self):
        self.car_speed+= MOVE_INCREMENT







