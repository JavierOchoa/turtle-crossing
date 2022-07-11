from turtle import Turtle, shapesize, Screen
import random
import time
COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10
screen = Screen()

class CarManager():
    def __init__(self):
        self.all_cars = []
        self.car_speed = STARTING_MOVE_DISTANCE
        
    def create_car(self):
        random_chance = random.randint(1, 6)
        if random_chance == 1:
            new_car = Turtle('square')
            new_car.color(random.choice(COLORS))
            new_car.shapesize(1, 3)
            new_car.penup()
            new_y = random.randint(-250, 230)
            new_car.goto(290, new_y)
            self.all_cars.append(new_car)

    def move_car(self):
        for car in self.all_cars:
            car.backward(self.car_speed)
            
    def more_speed(self):
        self.car_speed += MOVE_INCREMENT
        