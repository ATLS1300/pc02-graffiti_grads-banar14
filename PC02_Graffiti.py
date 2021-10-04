#!/usr/bin/env python
# coding: utf-8

'''
Turtle starter code
ATLS 1300
Author: Dr. Z
Author: YOUR NAME
May 29, 2020
'''

import turtle #import the library of commands that you'd like to use

turtle.colormode(255)

# Create a panel to draw on. 
panel = turtle.Screen()
w = 750 # width of panel
h = 750 # height of panel
panel.setup(width=w, height=h) #600 x 600 is a decent size to work on. 
#You can experiment by making it the size of your screen or super tiny!

# Create a colorful background and add Bezos image to it
image = "Bezos.gif"
panel.bgcolor("lightsteelblue1")
panel.bgpic(image)

#=======Add your code here======

#definitions


leftLip = (-6, 49)
midLeftTongue = (5, 25)
midRightTongue = (33, 28)
rightLip = (38, 53)
curveTongue = (19, 14)
tongueLineBottom = (23, 15)
tongueLineTop = (16, 51)
hatLeft = (-95, 177)
hatRight = (25, 205)
hatTop = (-60, 330)
dot1 = (-80, 185)
dot2 = (-30, 250)
dot3 = (-55, 280)
dot4 = (-35, 215)
fingertip = (111,-90)
magic1 = (150, -60)
magic2 = (230, -130)
magic3 = (300, -95)
magic4 = (365, -210)
tonguePen = (3)
magic1Pen = (8)
magic2Pen = (20)
magic3Pen = (30)
magic4Pen = (40)
hatPen = (5)
dotPen = (2)
dotSize = (10)



#hat

turtle.up()

turtle.goto(hatLeft)

turtle.color(143,0,255)

turtle.pensize(hatPen)

turtle.down()

turtle.begin_fill()

turtle.goto(hatRight)

turtle.goto(hatTop)

turtle.goto(hatLeft)

turtle.end_fill()

turtle.up()


#dots on hat

turtle.goto(dot1)

turtle.pensize(dotPen)

turtle.color(255,255,255)

turtle.down()

turtle.circle(dotSize)

turtle.up()

turtle.goto(dot2)

turtle.down()

turtle.circle(dotSize)

turtle.up()

turtle.goto(dot3)

turtle.down()

turtle.circle(dotSize)

turtle.up()

turtle.goto(dot4)

turtle.down()

turtle.circle(dotSize)

turtle.up()


#magic

turtle.goto(fingertip)

turtle.color(254,222,23)

turtle.pensize(magic1Pen)

turtle.down()

turtle.goto(magic1)

turtle.pensize(magic2Pen)

turtle.goto(magic2)

turtle.pensize(magic3Pen)

turtle.goto(magic3)

turtle.pensize(magic4Pen)

turtle.goto(magic4)

turtle.up()


#tongue

turtle.up()

turtle.goto(leftLip)

turtle.color(209,144,142)

turtle.down()

turtle.pensize(tonguePen)

turtle.begin_fill()

turtle.goto(midLeftTongue)

turtle.goto(midRightTongue)

turtle.goto(rightLip)

turtle.end_fill()

turtle.up()

turtle.goto(curveTongue)

turtle.down()

turtle.begin_fill()

turtle.circle(15)

turtle.end_fill()

turtle.up()

turtle.goto(tongueLineBottom)

turtle.color(0,0,0)

turtle.pensize(1)

turtle.down()

turtle.goto(tongueLineTop)

turtle.hideturtle()


#=======Clean up code (do not change)======
# this code ensures that your script runs correctly each time.
turtle.done()
