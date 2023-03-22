from turtle import *
pensize(2)
speed(10)

def drawsquare():
    forward(100)    
    left(70)   

def drawtriangle():
    right(50)
    forward(80)
    left(100)
    forward(75)
    left(40)
    forward(104)

def drawdoor():
    left(90)
    forward(65)
    left(90)
    forward(50)
    left(90)
    forward(25)
    left(90)
    forward(50)

def drawtree():
    right(90)
    forward(200)

    right(90)
    forward(50)

    right(90)
    circle(20)

def drawhouse():
    for prop in range(6):
        drawsquare()
        left(20)
    drawtriangle()
    drawdoor()
    drawtree()



author = "jeffrey"

if __name__ == "__main__":
    drawhouse()

    exitonclick()