import turtle

screen = turtle.Screen()
screen.title('Spiral of Spirals Fractal - PythonTurtle.Academy')
screen.setup(1000, 1000)
screen.setworldcoordinates(-1000, -1000, 1000, 1000)
turtle.speed(0)
turtle.hideturtle()
screen.tracer(0, 0)


def draw_spiral(x, y, length, direction):
    L = length
    for _ in range(50):
        if length > 5:
            draw_spiral(x, y, length * 0.27, direction - 30)
        turtle.up()
        turtle.seth(direction)
        turtle.goto(x, y)
        if length <= 5: turtle.down()
        turtle.fd(length)
        x, y = turtle.xcor(), turtle.ycor()
        length *= 0.93
        direction += 20


draw_spiral(-800, 700, 400, -90)
screen.update()
ts = turtle.getscreen()
ts.getcanvas().postscript(file="spiral.eps")
