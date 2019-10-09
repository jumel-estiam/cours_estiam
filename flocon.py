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


flocon(2,120)
