from turtle import *

def flocon(l):
    motif(l)
    left(120)
    motif(l)
    left(120)
    motif(l)
    left(120)


def motif(l):
    forward(l/3)
    right(60)
    forward(l/3)
    left(120)
    forward(l/3)
    right(60)
    forward(l/3)


flocon(120)
