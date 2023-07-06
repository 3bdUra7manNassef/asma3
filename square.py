
#todo we want drowning a dream square 

#* import turtle module
import turtle

#* create a Screen object
wind = turtle.Screen()
wind.setup(500, 500)
wind.bgcolor('black')

#* create a Turtle object
abo_grgr1 = turtle.Turtle()
abo_grgr1.speed(0)
abo_grgr1.color('#FFE4C4')
abo_grgr1.penup()
abo_grgr1.goto(100, 100)
abo_grgr1.pendown()
abo_grgr1.pensize(3)

abo_grgr2 = turtle.Turtle()
abo_grgr2.speed(0)
abo_grgr2.color('#EED5B7')
abo_grgr2.penup()
abo_grgr2.goto(70, 70)
abo_grgr2.pendown()
abo_grgr2.pensize(3)

abo_grgr3 = turtle.Turtle()
abo_grgr3.speed(0)
abo_grgr3.color('#CDB79E')
abo_grgr3.penup()
abo_grgr3.goto(50, 50)
abo_grgr3.pendown()
abo_grgr3.pensize(3)

abo_grgr4 = turtle.Turtle()
abo_grgr4.speed(0)
abo_grgr4.color('#8B7D6B')
abo_grgr4.penup()
abo_grgr4.goto(20, 20)
abo_grgr4.pendown()
abo_grgr4.pensize(3)

running_right = 90
running_fd = 250

# draw a square
for i in range(running_fd):
    abo_grgr1.right(running_right-1)
    abo_grgr1.fd(running_fd-1)
    abo_grgr2.right(running_right-1)
    abo_grgr2.fd(running_fd-1)
    abo_grgr3.right(running_right-1)
    abo_grgr3.fd(running_fd-1)
    abo_grgr4.right(running_right-1)
    abo_grgr4.fd(running_fd-1)

turtle.mainloop()