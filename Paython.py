import turtle   #module

wind=turtle.Screen()  #object
wind.bgcolor("black")  #back_ground
wind.title("ping pong")   #head
wind.setup(width=800,height=600)   #dimention
wind.tracer(0)          #control
 #madrab1
madrab1 =turtle.Turtle()
madrab1.speed(0)
madrab1.color("blue")
madrab1.shape("square")
madrab1.shapesize(stretch_wid=5,stretch_len=1)
madrab1.penup()
madrab1.goto(-350,0)
#madrab2
madrab2 =turtle.Turtle()
madrab2.speed(0)
madrab2.color("Red")
madrab2.shape("square")
madrab2.shapesize(stretch_wid=5,stretch_len=1)
madrab2.penup()
madrab2.goto(350,0)
#ball
ball =turtle.Turtle()
ball.speed(0)
ball.color("white")
ball.shape("circle")
ball.penup()
ball.goto(0,0)
ball.dx=.5
ball.dy=.5

#Score
#variable
score1=0
score2=0
score=turtle.Turtle()
score.color("white")
score.penup()
score.speed(0)
score.hideturtle()
score.goto(0,250)
score.write("player1:0,player2:0", align="center",font= ("courier",24,"normal"))




#up
def madrab1_up():
    y=madrab1.ycor()
    y +=20
    madrab1.sety(y)
#down
def madrab1_down():
    y=madrab1.ycor()
    y -=20
    madrab1.sety(y)
#up2
def madrab2_up():
    y=madrab2.ycor()
    y +=20
    madrab2.sety(y)
#down2
def madrab2_down():
    y=madrab2.ycor()
    y -=20
    madrab2.sety(y)




wind.listen()
wind.onkeypress(madrab1_up,"a")
wind.onkeypress(madrab1_down,"q")
wind.onkeypress(madrab2_up,"Up")
wind.onkeypress(madrab2_down,"Down")

#ball managment


while True :
    wind.update()
    ball.setx(ball.xcor() +ball.dx)
    ball.sety(ball.ycor() +ball.dy)
    if ball.ycor()>290:
        ball.sety(290)
        ball.dy *= -1
    if ball.ycor()<-290:
        ball.sety(-290)
        ball.dy *= -1
    if ball.xcor()>390:
        ball.goto(0,0)
        ball.dx *= -1
        score1+=1
        score.clear()
        score.write("player1:{},player2:{}" .format(score1,score2), align="center", font=("courier", 24, "normal"))

    if ball.xcor()<-390:
        ball.goto(0,0)
        ball.dx *=-1
        score2+=1
        score.clear()
        score.write("player1:{},player2:{}".format(score1, score2), align="center", font=("courier", 24, "normal"))

    if (ball.xcor() >340 and ball.xcor()<350 and ball.ycor()<madrab2.ycor()+40 and ball.ycor()>madrab2.ycor()-40):
        ball.setx(340)

        ball.dx *=-1

    if( ball.xcor() <- 340 and ball.xcor() >- 350 and ball.ycor() < madrab2.ycor() + 40 and ball.ycor() > madrab2.ycor() - 40):
        ball.setx(-340)
        ball.dx *= -1



