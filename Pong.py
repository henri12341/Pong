import turtle

window = turtle.Screen()
window.title("Pong")
window.bgcolor("black")
window.setup(width=800, height=600)
window.tracer(0)

# Padlle A
paddle_a = turtle.Turtle()
paddle_a.speed(0)
paddle_a.color("white")
paddle_a.shape("square")
paddle_a.shapesize(stretch_wid=5, stretch_len=1)
paddle_a.penup()
paddle_a.goto(-350,0)

# Padlle B
paddle_b = turtle.Turtle()
paddle_b.speed(0)
paddle_b.color("white")
paddle_b.shape("square")
paddle_b.shapesize(stretch_wid=5, stretch_len=1)
paddle_b.penup()
paddle_b.goto(350,0)

# Ball
ball = turtle.Turtle()
ball.speed(0)
ball.color("white")
ball.shape("circle")
ball.penup()
ball.goto(0,0)
ball.dx = 0.2
ball.dy = 0.1

# Paddle movement
def paddle_a_up():
    y = paddle_a.ycor()
    y += 20
    print("kutsuttu")
    paddle_a.sety(y)

def paddle_a_down():
    y = paddle_a.ycor()
    y -= 20
    paddle_a.sety(y)

def paddle_b_up():
    y = paddle_b.ycor()
    y += 20
    paddle_b.sety(y)

def paddle_b_down():
    y = paddle_b.ycor()
    y -= 20
    paddle_b.sety(y)

if __name__ == '__main__':
    # Key listeners
    window.listen()
    window.onkeypress(paddle_a_up, "w")
    window.onkeypress(paddle_a_down, "s")
    window.onkeypress(paddle_b_up, "Up")
    window.onkeypress(paddle_b_down, "Down")

    # Main loop
    while True:
        window.update()

        # Moving ball
        ball.setx(ball.xcor() + ball.dx)
        ball.sety(ball.ycor() + ball.dy)

        # Border checks

        if ball.ycor() > 290:
            ball.dy *= -1

        if ball.ycor() < -290:
            ball.dy *= -1

        if ball.xcor() > 390:
            ball.goto(0,0)
            ball.dx *= -1

        if ball.xcor() < -390:
            ball.goto(0,0)
            ball.dx *= -1

        # Paddle and ball collision

        if ball.xcor() > 340 and (ball.ycor() < paddle_b.ycor() + 50) and\
                (ball.ycor() > paddle_b.ycor() - 50):
            ball.dx *= -1.0

        if ball.xcor() < -340 and (ball.ycor() < paddle_a.ycor() + 50) and\
                (ball.ycor() > paddle_a.ycor() - 50):
            ball.dx *= -1.0



