import turtle as t

t.setup(1000, 600)
t.pensize(2)
t.pencolor('black')
t.speed(5)

t.seth(60)
t.forward(300)
t.seth(-60)
t.forward(300)
t.seth(180)
t.forward(300)

t.penup()
t.seth(60)
t.forward(150)
t.pendown()
t.seth(0)
t.forward(150)
t.seth(-120)
t.forward(150)
t.seth(120)
t.forward(150)

t.done()