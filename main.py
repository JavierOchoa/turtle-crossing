import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

scoreboard = Scoreboard()

screen = Screen()
screen.title('Turtle Crossing Game')
screen.setup(width=600, height=600)
screen.tracer(0)
screen.listen()

car_manager = CarManager()
player = Player()
screen.onkey(player.move_up, 'Up')
screen.onkey(player.move_down, 'Down')
screen.onkey(player.move_left, 'Left')
screen.onkey(player.move_right, 'Right')



game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()
    
    car_manager.create_car()
    car_manager.move_car()
    
    for car in car_manager.all_cars:
        if car.distance(player) < 35:
            game_is_on = False
            scoreboard.game_over()
    
    if player.ycor() >= 250:
        scoreboard.plus_one()
        player.goto(0, -280)
        car_manager.more_speed()
    

