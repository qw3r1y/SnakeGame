import turtle
import time 
import random 

hiz = 0.15
pencere = turtle.Screen()
pencere.title("YILAN OYUNU")
pencere.bgcolor("black")
pencere.setup(width=600,height=600)

pencere.tracer(0)


kafa = turtle.Turtle()

kafa.speed(0)
kafa.shape("triangle")
kafa.color("orange")
kafa.penup()
kafa.goto(0,100)
kafa.direction = "stop"

yemek = turtle.Turtle()


yemek.speed(0)
yemek.shape("circle")
yemek.color("yellow")
yemek.penup()
yemek.goto(0,0)
yemek.shapesize(0.80,0.80)

kuyruklar = []

puan = 0

yazı = turtle.Turtle()


yazı.speed(0)
yazı.shape("square")
yazı.color("white")
yazı.penup()
yazı.goto(0,260)
yazı.hideturtle()
yazı.write("SİNEMİSLE ÇOCUK SAYINIZ :D: {}".format(puan), align="center", font=("Courier", 24, "normal"))


def move():

    if kafa.direction == "up":
        y = kafa.ycor()    
        kafa.sety(y +20)
    if kafa.direction == "down":
        y = kafa.ycor()    
        kafa.sety(y -20)

    if kafa.direction == "right":
        x = kafa.xcor()    
        kafa.setx(x +20)

    if kafa.direction == "left":
        x = kafa.xcor()    
        kafa.setx(x - 20)
def goUp():
    kafa.setheading(90) 
    if kafa.direction != "down":
        kafa.direction = "up"

def goLeft():
    kafa.setheading(90) 
    if kafa.direction != "right":
        kafa.direction = "left"

def goRight():
    kafa.setheading(90) 
    if kafa.direction != "left":
        kafa.direction = "right"


def goDown():
    kafa.setheading(90) 
    if kafa.direction != "up":
        kafa.direction = "down"
pencere.listen()
pencere.onkey(goUp, "Up")
pencere.onkey(goDown, "Down")
pencere.onkey(goRight, "Right")
pencere.onkey(goLeft, "Left")



while True:
    pencere.update()


    if kafa.xcor() > 300 or kafa.xcor() < -300 or kafa.ycor() > 300 or kafa.ycor()< -300:
        time.sleep(1)
        kafa.goto(0,0)
        kafa.direction = "stop"

        for kuyruk in kuyruklar:
            kuyruk.goto(1000,1000)

        kuyruklar= []
        puan = 0
        yazı.clear()
        yazı.write("SİNEMİSLE ÇOCUK SAYINIZ :D: {}".format(puan), align="center", font=("Courier", 24, "normal"))

        hiz = 0.15

    if kafa.distance(yemek) < 20 :
        x = random.randint(-250,250)
        y = random.randint(-250,250)

        yemek.goto(x, y)


        puan = puan + 10
        yazı.clear()
        yazı.write("SİNEMİSLE ÇOCUK SAYINIZ :D: {}".format(puan), align="center", font=("Courier", 24, "normal"))


        hiz = hiz + 0.002


        yeniKuyruk = turtle.Turtle()
        yeniKuyruk.speed(0)
        yeniKuyruk.shape("circle")
        yeniKuyruk.color("red")
        yeniKuyruk.penup()
        kuyruklar.append(yeniKuyruk)


    for i in range(len(kuyruklar )-1,0,-1):
        x = kuyruklar[i - 1].xcor()
        y = kuyruklar[i - 1].ycor()
        kuyruklar[i].goto(x,y)

    if len (kuyruklar)> 0 :
        x = kafa.xcor()
        y = kafa.ycor()
        kuyruklar[0].goto(x,y)


    

    move()

    for segment in kuyruklar:
        if segment.distance(kafa) < 20:
            time.sleep(1)
            kafa.goto(0, 0)
            kafa.direction = "stop"
            for segment in kuyruklar:
                segment.goto(1000, 1000)
            kuyruklar = []
            puan = 0
            yazı.clear()
            yazı.write('Puan: {}'.format(puan), align='center', font=('Courier', 24, 'normal'))
            hiz = 0.15


    time.sleep(hiz)
