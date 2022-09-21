from turtle import Screen
from ball import Ball
from paddle import Paddle
from brick import Brick
from scoreboard import Scoreboard
import time



screen = Screen()
screen.setup(width=600, height=510)
screen.bgcolor('white')
screen.title('Break Game')
screen.tracer(0)




ball = Ball()
ball2 = Ball()
paddle = Paddle((0, -200))
scoreboard = Scoreboard()
x = 0
brick1_list = []
brick2_list = []
brick3_list = []
brick4_list = []
brick5_list = []


for i in range(11):
    brick1 = Brick((-270 + x,200))
    brick1_list.append(brick1)
    brick2 = Brick((-270 + x,170))
    brick2_list.append(brick2)
    brick3 = Brick((-270 + x,140))
    brick3_list.append(brick3)
    brick4 = Brick((-270 + x,110))
    brick4_list.append(brick4)
    brick5 = Brick((-270 + x,80))
    brick5_list.append(brick5)
    x += 54

print(brick1_list)

screen.listen()
screen.onkeypress(paddle.move_left, "Left")
screen.onkeypress(paddle.move_right, "Right")

ball2.ht()
game_is_on = True
while game_is_on:
    time.sleep(ball.move_speed)
    screen.update()
    ball.move()

    for i in range(11):
        if ball.distance(brick1_list[i]) < 30:
            ball.hit_brick_y()
            brick1_list[i].ht()
            brick1_list[i].goto(500,500)
            scoreboard.score()
            print(brick1_list)


    for i in range(11):
        if ball.distance(brick2_list[i]) < 30:
            ball.hit_brick_y()
            brick2_list[i].ht()
            brick2_list[i].goto(500,500)
            scoreboard.score()
            print(brick2_list)


    for i in range(11):
        if ball.distance(brick3_list[i]) < 30:
            ball.hit_brick_y()
            brick3_list[i].ht()
            brick3_list[i].goto(500,500)
            scoreboard.score()
            print(brick3_list)

    for i in range(11):
        if ball.distance(brick4_list[i]) < 30:
            ball.hit_brick_y()
            brick4_list[i].ht()
            brick4_list[i].goto(500,500)
            scoreboard.score()
            print(brick4_list)

    for i in range(11):
        if ball.distance(brick5_list[i]) < 30:
            ball.hit_brick_y()
            brick5_list[i].ht()
            brick5_list[i].goto(500,500)
            scoreboard.score()
            print(brick5_list)

    if ball.xcor()>280 or ball.xcor()<-280:
        ball.hit_wall()

    if paddle.xcor()-30 < ball.xcor() < paddle.xcor()+30 and ball.ycor() < -180:
        ball.bounce()

    if ball.ycor() > 220:
        ball.bounce()

    if ball.ycor() < -225:
        print('Game over!')
        game_is_on = False
        ball2.goto(0,0)
        scoreboard.clear()
        ball2.write(f'Game Over!', font=('Arial', 20, 'normal'), align='center')
        ball2.goto(0, -30)
        ball2.write(f'Your score is: {scoreboard.points}!', font=('Arial', 20, 'normal'), align='center')

    if scoreboard.points == 55:
        print('You won!')
        game_is_on = False
        ball2.ht()
        ball2.goto(0, 0)
        scoreboard.clear()
        ball2.write(f'You won!', font=('Arial', 20, 'normal'), align="center")
        ball2.goto(0, -30)
        ball2.write(f'New levels coming soon!', font=('Arial', 20, "normal"), align="center")


    screen.update()



screen.exitonclick()