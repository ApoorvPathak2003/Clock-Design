import turtle, time

screen = turtle.Screen()
screen.setup(800, 600)
screen.bgcolor("black")
screen.title("Analog Clock")
screen.tracer(0)

pen = turtle.Turtle()
pen.hideturtle()
pen.speed(0)
pen.pensize(5)

def drawClock(hours, minutes, seconds):
    
    pen.penup()
    pen.goto(0, 150)
    pen.setheading(180)
    pen.color("red")
    pen.pendown()
    pen.circle(150)
    
    pen.penup()
    pen.goto(0, 0)
    pen.setheading(90)

    for i in range(12):
        pen.forward(135)
        pen.pendown()
        pen.forward(15)
        pen.penup()
        pen.goto(0, 0)
        pen.rt(30)   

    pen.color("blue")
    pen.setheading(90)
    angle = (hours / 12) * 360
    pen.rt(angle)
    pen.pendown()
    pen.forward(75)   
    pen.penup() 
    pen.goto(0, 0)
    
    pen.color("yellow")
    pen.setheading(90)
    angle = (minutes / 60) * 360
    pen.rt(angle)
    pen.pendown()
    pen.forward(90) 
    pen.penup()
    pen.goto(0, 0)

    pen.color("green")
    pen.setheading(90)
    angle = (seconds / 60) * 360
    pen.rt(angle)
    pen.pendown()
    pen.forward(120)  

while True:
    hours = int(time.strftime("%I"))
    minutes = int(time.strftime("%M"))
    seconds = int(time.strftime("%S"))

    drawClock(hours, minutes, seconds)
    screen.update()

    time.sleep(1)

    pen.clear()