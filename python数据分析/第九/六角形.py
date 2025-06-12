import turtle as t
t.setup(1000, 600)
t.pensize(2)
t.pencolor('black')

t.seth(30)
t.fd(210)
t.seth(-90)
t.fd(210)
t.seth(150)
t.fd(210)

t.seth(30)
t.penup()
t.fd(70)
t.seth(90)
t.fd(70)
t.pendown()

t.seth(-30)
t.fd(210)
t.seth(-150)
t.fd(210)
t.seth(90)
t.fd(210)

t.done()