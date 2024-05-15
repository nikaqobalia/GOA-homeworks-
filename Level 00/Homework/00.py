from turtle import *

#we want to paint a hous

#step 1:  draw a square
speed(30)
width(7)
color("blue")
forward(200)
left(90)

forward(200)
left(90)

forward(200)
left(90)

forward(200)
left(90)
#end of square

#drawing a door
begin_fill()

forward(70)
color("red")
left(90)
forward(100)
right(90)
forward(60)
right(90)
forward(100)
end_fill()
penup()
goto(200, 200)
pendown()

color("yellow")
begin_fill()
right(150)
forward(200)
left(120)
forward(200)
end_fill()

lenght = 40
anglerotate = 90
penup() 

color("brown")
goto(175, 125)
pendown()
begin_fill()
color("brown")
begin_fill()
left(210)
forward(lenght)
left(anglerotate)
forward(lenght)
left(anglerotate)
forward(lenght)
left(anglerotate)
forward(lenght)
left(anglerotate)
end_fill()

penup()

goto(70, 125)
pendown()
begin_fill()
color("brown")
forward(lenght)
left(anglerotate)
forward(lenght)
left(anglerotate)
forward(lenght)
left(anglerotate)
forward(lenght)
left(anglerotate)
end_fill()
penup()




exitonclick()