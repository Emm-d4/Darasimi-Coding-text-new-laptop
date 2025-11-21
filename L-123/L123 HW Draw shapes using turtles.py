import turtle

turtle.Screen().bgcolor("Gold")
paper =turtle.Screen()
paper.setup(700,500)

pen = turtle.Turtle()

# pentagone
angle3 = 360/5
pen.forward(100)

pen.left(angle3)
pen.forward(100)

pen.left(angle3)
pen.forward(100)

#move position
pen.penup()
pen.left(120)
pen.forward(200)

#start to draw
pen.pendown()

# hexagone
angle4 = 360/6
pen.forward(100)
pen.left(angle6)

pen.forward(100)
pen.left(angle6)

pen.forward(100)
pen.left(angle6)

pen.forward(100)
pen.left(angle6)

turtle.done()