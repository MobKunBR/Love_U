from turtle import *
speed(1)
color("dark red")
begin_fill()
pensize(4)
left(50)
forward(133)
circle(50,200)
right(140)
circle(50,200)
forward(260)
end_fill()
left(100)
for i in range(10):
    write("I love U", move=True, align="left")
    forward(25)     