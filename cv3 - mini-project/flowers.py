import turtle           # Importuje príkazy k knižnice turtle.                                                   
from polygon import arc # Importuje funkciu arc zo skriptu polygon.py.

turtle.delay(3) # Rýchle vykreslenie funkcie.
  
# Nakreslí n úsečiek.
#   angle: (uhol) stupne medzi úsečkami.
#   length: (dĺžka) každej úsečky.             
def polyline(angle,length):
    for i in range(length):
        turtle.forward(length)
        turtle.left(angle)

# Vykreslí lupeň/lístok.
#   angle: (uhol) stupne medzi úsečkami.
#   length: (dĺžka) každej úsečky.
def petal(angle,length):
    for i in range(2):
        polyline(angle,length)
        turtle.left(180-angle*length)

# Vykreslí hlavu kvetu (lupeňe).
#   angle: (uhol) stupne medzi úsečkami.
#   length: (dĺžka) každej úsečky.
#   count: (počet) lupienkov na kvete.
def flower(angle,length,count):
    for i in range(count):
        petal(angle,length)
        turtle.left(360/count)

# Vykreslí stonku kvetu.
#   angle: (uhol) stupne medzi úsečkami.
#   length: (dĺžka) každej úsečky.
#   anglePetal: Uhol lístku na stonke.
#   lengthPetal: Dĺžka lístku na stonke.
#   spacing: Rozostup medzi lístkami na stonke.
#   angleStem: Uhol stonky. 
#   lengthStem: Dĺžka stonky.
def stem(anglePetal,lengthPetal,spacing,angleStem,lengthStem):
    turtle.seth(-90-angleStem/2) 
    arc(turtle,lengthStem,angleStem)
    turtle.seth(80)
    petal(-anglePetal,lengthPetal)
    turtle.seth(spacing)
    petal(anglePetal,lengthPetal)

# Zabezpečí medzery medzi kvetinami.
#   x: pohyb na ose x (horizontálne).
#   y: pohyb na ose y (vertikálne).
def move(x,y):    
    turtle.pu()
    turtle.goto(x,y)
    turtle.pd()

# Vykreslí celú kvetinu podľa zadaných hodnôt.
#   angle: (uhol) stupne medzi úsečkami.
#   length: (dĺžka) každej úsečky.
#   count: (počet) lupienkov na kvete.
#   anglePetal: Uhol lístku na stonke.
#   lengthPetal: Dĺžka lístku na stonke.
#   spacing: Rozostup medzi lístkami na stonke.
#   angleStem: Uhol stonky.
#   lengthStem: Dĺžka stonky.
def full_flower(angle, length, count, anglePetal, lengthPetal, spacing, angleStem, lengthStem):
    flower(angle,length,count)
    stem(anglePetal,lengthPetal,spacing, angleStem,lengthStem)

#flower 1
move(-300,0)
full_flower(6,9,7,8,9,102,90,125)

#flower 2
move(0,0)
full_flower(8,9,10,2,12,102,56,300)

#flower 3
move(300,0)
full_flower(2,8,20,6,13,102,30,350)
  
turtle.hideturtle() # Schová korytnačku po dokončení funkcie
turtle.mainloop() # Turtle graphic interface počká na akciu používateľa