import turtle as t
import random as rand

my_turtle = t.Turtle()
my_turtle.shape("turtle")


colors = ["CornflowerBlue", "DarkOrchid", "IndianRed", "DeepSkyBlue", "LightSeaGreen", "wheat", "SlateGray", "SeaGreen"]

"""

'''Draw a square using loop'''
for _ in range(4):
    my_turtle.forward(100)
    my_turtle.right(90)


'''Draw a dash line'''
for _ in range(50):
    my_turtle.forward(5)
    my_turtle.penup()
    my_turtle.forward(5)
    my_turtle.pendown()
    


#draw different shapes
def draw_shape(num_sides):
    angle = 360 / num_sides
    for _ in range(num_sides):
        my_turtle.forward(100)
        my_turtle.right(angle)
        
for sides in range(3, 11):
    my_turtle.pencolor(rand.choice(colors))
    draw_shape(sides)
    

for i in range(8):
    t.colormode(255)
    my_turtle.pencolor(rand.randint(1,255),rand.randint(1,255),rand.randint(1,255))
    for _ in range(i+3):
        my_turtle.forward(100)
        my_turtle.right(360/(i+3))
"""
t.colormode(255)

def random_color():
    r = rand.randint(0,255)
    g = rand.randint(0,255)
    b = rand.randint(0,255)
    color = (r, g, b)
    return color

"""
directions = [0, 90, 180, 270]
my_turtle.pensize(20)
my_turtle.speed("fastest")

for _ in range(200):
    my_turtle.pencolor(random_color())
    my_turtle.forward(30)
    my_turtle.setheading(rand.choice(directions))

"""
my_turtle.speed("fastest")

def draw_spirograph(gap_size):
    for _ in range(int(360 / gap_size)):
        my_turtle.color(random_color())
        my_turtle.circle(200)
        my_turtle.setheading(my_turtle.heading() + gap_size)
        my_turtle.forward(gap_size)
        
draw_spirograph(5)


screen = t.Screen()
screen.exitonclick()