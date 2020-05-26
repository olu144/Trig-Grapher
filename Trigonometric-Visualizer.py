import math
import turtle

def main():
    fred=turtle.Turtle()
    wn=turtle.Screen()
    setUpWindow(wn)
    setUpTurtle(fred)
    drawSine(fred)
    drawCosineCurve(fred)   
    drawTangentCurve(fred)
    drawNaturalLog(fred)
    wn.exitonclick()

def setUpWindow(screen_object):
    screen_object=turtle.Screen()
    screen_object.setworldcoordinates(-360,-1,360,1)
    screen_object.bgcolor("orange")

def setUpTurtle(turtle_object):
    turtle_object.goto(0,-1)
    turtle_object.goto(0,1)
    turtle_object.up()
    turtle_object.goto(360,0)   
    turtle_object.down()
    turtle_object.goto(-360,0)
    turtle_object.shape('turtle')

def drawSine(turtle_object):
    for i in range (-360,360):
            turtle_object.goto(i,math.sin(math.radians(i)))
            turtle_object.down()
    turtle_object.up()	

def drawCosineCurve(turtle_object):
    for i in range (-360,360):
            turtle_object.goto(i,math.cos(math.radians(i)))
            turtle_object.down()
    turtle_object.up()
	
def drawTangentCurve(turtle_object):
    turtle_object.speed(0)
    for i in range (-360,360):
            turtle_object.goto(i,math.tan(math.radians(i)))
            turtle_object.down()
    turtle_object.up()
	
def drawNaturalLog(turtle_object):
    for i in range (0,360):
            turtle_object.goto(i,math.log1p(math.radians(i)))
            turtle_object.down()
    turtle_object.up()

main()
