import turtle

def draw_square():
    brad = turtle.Turtle()
    brad.shape("turtle")
    brad.color("yellow")
    brad.speed(2)

    sides_count = 0
    num_sides = 4

    while (sides_count < num_sides):
        brad.forward(100)
        brad.right(90)
        sides_count = sides_count + 1

def draw_circle():
    angie = turtle.Turtle()
    angie.shape("arrow")
    angie.color("blue")
    angie.circle(100)

def draw_triangle():
    thaddeus = turtle.Turtle()
    thaddeus.shape("classic")
    thaddeus.color("green")

    sides_count = 0
    num_sides = 3

    while (sides_count < num_sides):
        thaddeus.back(100)
        thaddeus.left(120)
        sides_count = sides_count + 1

def draw_shapes():
    window = turtle.Screen()
    window.bgcolor("red")
    draw_square()
    draw_circle()
    draw_triangle()
    window.exitonclick()

draw_shapes()
