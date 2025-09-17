import turtle
turtle.Screen().bgcolor("Aqua")
turtle.Screen().setup(300,400)
polygon=turtle.Turtle()
num_sides=4
angle=360.0/num_sides
side_length=100
for sides in range(num_sides):
    polygon.forward(side_length)
    polygon.right(angle)
turtle.done()    