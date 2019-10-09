from turtle import *

def sierpinski(n, l):
    color('black')
    begin_fill()
    if n == 0:
        for i in range(0,3):
            forward(l)
            left(120)
    else:
        sierpinski(n-1, l/2)
        forward(l/2)
        sierpinski(n-1, l/2)
        backward(l/2)
        left(60)
        forward(l/2)
        right(60)
        sierpinski(n-1, l/2)
        left(60)
        backward(l/2)
        right(60)
    end_fill()

ht()
speed(0)
tracer(8,25)


sierpinski(7,243)
