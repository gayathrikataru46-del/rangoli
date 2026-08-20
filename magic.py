import turtle as tur
tur.setup(800,800)
tur.speed(0)
tur.width(2)
tur.bgcolor("black")
tur.color("white")
for j in range(25):
    for i in range(25):
        tur.right(90)
        tur.circle(200-i*8,90)
        tur.left(90)
        tur.circle(200-i*8,90)
        tur.right(180)
        tur.circle(50,4,4)
tur.hideturtle()
tur.done()