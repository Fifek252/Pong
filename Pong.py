import turtle


wn = turtle.Screen()
wn.title("Pong")
wn.bgcolor("grey")
wn.setup(width = 800,height = 600)
wn.tracer(0)


# Paddle A
pad_a = turtle.Turtle()
pad_a.speed(0)
pad_a.shape("square")
pad_a.color("green")
pad_a.penup()
pad_a.goto(-350,0)
pad_a.shapesize(stretch_wid=5,stretch_len=1)

# Paddle B
pad_b = turtle.Turtle()
pad_b.speed(0)
pad_b.shape("square")
pad_b.color("orange")
pad_b.penup()
pad_b.goto(350,0)
pad_b.shapesize(stretch_wid=5,stretch_len=1)

# Ball
ball = turtle.Turtle()
ball.speed(0)
ball.shape("circle")
ball.color("white")
ball.penup()
ball.goto(0,0)
ball.dx = 0.3
ball.dy = -0.3

# Movement of Paddle A
def pad_a_up():
    y = pad_a.ycor()
    y += 20
    pad_a.sety(y)

def pad_a_down():
    y = pad_a.ycor()
    y -= 20
    pad_a.sety(y)
    
# Movement of Paddle B
def pad_b_up():
    y = pad_b.ycor()
    y += 20
    pad_b.sety(y)

def pad_b_down():
    y = pad_b.ycor()
    y -= 20
    pad_b.sety(y)
    
# Pen
pen = turtle.Turtle()
pen.penup()
pen.speed(0)
pen.color("white")
pen.hideturtle()
pen.goto(0,260)
pen.write("Player A: 0  Player B: 0", align = 'center', font=("Courier",24,"normal"))

# Score
score_a = 0
score_b = 0
    
# Keyboard binding
wn.listen()
wn.onkeypress(pad_a_up,"w")
wn.onkeypress(pad_a_down,"s")
wn.onkeypress(pad_b_up,"Up")
wn.onkeypress(pad_b_down,"Down")


while True:
    wn.update()
    
    # Move the ball
    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)
    
    # Border checking for ball
    if ball.ycor() > 290:
        ball.sety(290)
        ball.dy *= -1
        
        
    if ball.ycor() < -290:
        ball.sety(-290)
        ball.dy *= -1
        
        
    if ball.xcor() > 390:
        score_a += 1
        ball.goto(0,0)
        ball.dx *= -1
        
        pen.clear()
        pen.write(f"Player A: {score_a}  Player B: {score_b}", align = 'center', font=("Courier",24,"normal"))
    
    if ball.xcor() < -390:
        score_b += 1
        ball.goto(0,0)
        ball.dx *= -1
        
        pen.clear()
        pen.write(f"Player A: {score_a}  Player B: {score_b}", align = 'center', font=("Courier",24,"normal"))

        
    # Border checking for pads
    if pad_a.ycor() < - 250:
        pad_a.sety(-250)
    if pad_a.ycor() > 250:
        pad_a.sety(250)
    if pad_b.ycor() < - 250:
        pad_b.sety(-250)
    if pad_b.ycor() > 250:
        pad_b.sety(250)
        
    # Bounce
    if (ball.xcor() > 340 and ball.xcor() < 350) and (ball.ycor()< pad_b.ycor() + 40 and ball.ycor() >= pad_b.ycor() - 40):
        ball.color("orange")
        
        ball.dx *= -1
        
    
    if (ball.xcor() < -340 and ball.xcor() > -350) and (ball.ycor() < pad_a.ycor() + 40 and ball.ycor()>= pad_a.ycor() - 40):
        ball.color("green")
        
        ball.dx *= -1