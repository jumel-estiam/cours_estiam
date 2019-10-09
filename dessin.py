from turtle import *

color('red','yellow')
begin_fill()
speed(25)
while True:
    forward(200)
    left(90)
    if abs(pos()) < 1:
        break
end_fill()

begin_fill()

left(90)
forward(200)
right(45)
forward(141)
right(90)
forward(141)

end_fill()


begin_fill()

left(135)
forward(141)
left(90)
forward(50)
left(90)
forward(100)

end_fill()


up()
bk(120)
right(90)
forward(150)
down()

positinInitialeSoleil = pos()
while True:
    forward(200)
    left(170)
    if abs(pos() - positinInitialeSoleil) < 1:
        break


from fonctions import *
triangle(100,100)

done()
