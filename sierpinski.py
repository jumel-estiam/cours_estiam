from turtle import *

ht()
speed(0)
tracer(8,25)

def sierpinski(n, l):
    color('black')
    begin_fill()
    if n == 0:
        for i in range(0,3):
            forward(l)
            left(120)
    else:
        pass
    end_fill()


sierpinski(0,243)
