#turtle-ში დახაზეთ სასახლე, მეფე და დედოფალი, დაარჭვეთ GOA-ს დროშა კოშკზე.
from turtle import *

speed(30)
penup()
goto(-150,-250)
pendown()
width(5)
color("blue")

#ვხაზავ კვადრატს სახლისთვის
forward(275)   #სიგანე 
left(90)
forward(250)   #სიმაღლე 

left(90)       
forward(275)

left(90)
forward(250)   #სიმაღლე 

#პატარა კოშკს ვუდგამ მარცხენა მხარეს
left(180)
forward(25)

left(90)
forward(150)  #პატარა კოშკის სიგანე 

right(90)
forward(225)  #პატარა კოშკის სიმაღლე

right(90)
#პატარა კოშკს ვუდგამ მარჯვენა მხარეს 
forward(575)  # სახლის სიგანე პატარა კოშკებტან ერთად

right(90)
forward(225)  #პატარა კოშკის სიმაღლე

right(90)
forward(150)  #პატარა კოშკის სიგანე

right(90)
#მარჯვენა პატარა კოშკს ვყოფ შუაში
forward(105)  #გაყოფის სიმაღლე

#მარჯვენა პატარა კოშკს ვყოფ შუაში
right(90)    
forward(150)  #მარჯვენა პატარა კოშკის გაყოფის სიგანე

right(90)
forward(105)  #მარჯვენა პატარა კოშის გაყოფის სიმაღლე

right(90)
penup()
forward(575)  #სახლის სიგანე პატარა კოშკებთან ერთად. წამოვედით მარცხენა პატარა კოშკთან
right(90)
forward(105)  #პატარა კოშკის გაყოფის სიმაღლე
right(90)
pendown()
forward(150)  #მარცხენა პატარა კოშკის გაყოფის სიგანე

#გადავდივარ მარცხენა დიდი კოშკის დასახაზად
penup()
goto(-300, -225)
pendown()

#ვხაზავ მარცხენა დიდ კოშკს
right(140)     #დახრის სიგრძე მარცხენა დიდი კოშკი
forward(50)
right(40)
forward(160)   #მარცხენა დიდი კოშკის სიგანე 
right(90)
forward(430)    #მარცხენა დიდი კოშკის სიმაღლე 
right(90)
forward(160)    #მარცხენა დიდი კოშკის სიგანე
right(90)
forward(430)    #მარცხენა დიდი კოშკის სიმაღლე 

#გადავდიავარ მარცხენა პატარა კოშკზე დიდი მარცხენა კოშკის მისაერთებლად
penup()
goto(-300,-0)
pendown()
left(180)
forward(155)    #მარცხენა პატარა ხოშკს მივუერთე მარცხენა დიდი კოშკი და მისი სიმაღლეა
left(65)       #მარცხენა დიდი კოშკის დახრის სიგრძე
forward(40)     #მარცხენა პატარა კოშკს მივუერთე მარცხენა დიდი კოშკი და მისი დახრის სიგრძეა

#მივდივარ მარცხენა დიდი კოშკის კოშკურის ასაშენებლად
penup()
left(25)
forward(160)
pendown()

#ვაშენებ კოშკურას გალავანს
right(35)
forward(25)

right(55)
forward(15)

right(90)
forward(217)

right(90)
forward(50)

penup()
left(180)
forward(50)
pendown()

left(130)
forward(50)

penup()
left(180)
forward(50)
pendown()

left(50)
forward(50)
left(90)
forward(25)
left(90)
forward(20)
right(90)
forward(20)
right(90)
forward(20)
left(90)
forward(25)

left(90)
forward(20)

right(90)
forward(20)

right(90)
forward(20)







exitonclick()