from turtle import *

def flocon(n,l):
    motif(n,l)
    left(120)
    motif(n,l)
    left(120)
    motif(n,l)
    left(120)


def motif(n, l):
    if n == 0:
        forward(l)
    else:
        motif(n-1,l/3)
        right(60)
        motif(n-1,l/3)
        left(120)
        motif(n-1,l/3)
        right(60)
        motif(n-1,l/3)


ht()
tracer(8,25)
speed(0)
flocon(7,729/3)
