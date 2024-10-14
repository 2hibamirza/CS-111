# Final Project
# CS 111, Reckinger
# Hiba Mirza
# 11/30/22
# Random items will come from the bottom of the conveyor belt
# Each item will go to its specific bin, after scanning through the scanner

import turtle
import random

s = turtle.getscreen()
s.screensize(canvwidth=400, canvheight=400, bg='old lace')
s.title("Library Return Center")
turtle.addshape('book.gif')
turtle.addshape('dvd.gif')
turtle.addshape('magazine.gif')

# creates and customizes turtle
t = turtle.Turtle()
turtle.colormode(255)
t.hideturtle()
t.pencolor('black')
t.fillcolor('tan')
t.penup()
t.speed(5)
t.goto(-130, 120)

# makes 3 tan bins
t.begin_fill()
for i in range (3):
	# makes a tan bin
	for i in range (4):
		t.pendown()
		t.forward(60)
		t.left(90)
	t.penup()
	t.forward(100)
t.end_fill()

t.goto(-115, 120)
t.fillcolor('black')
t.begin_fill()
# makes a hole for all 3 bins
for i in range (3):
	# makes a hole
	for i in range (4):
		t.pendown()
		t.forward(30)
		t.left(90)
	t.penup()
	t.forward(100)
t.end_fill()

# labels bins and creates title
text = turtle.Turtle()
text.penup()
text.hideturtle()
text.goto(0, 190)
text.pencolor('red')
text.write("Library Return Center", align='center', font=('Times New Roman', 12, 'bold'))
text.goto(-100, 160)
text.pencolor('black')
text.write("Books", align='center', font=('Times New Roman', 8, 'bold'))
text.goto(0, 160)
text.write("DVDs", align='center', font=('Times New Roman', 8, 'bold'))
text.goto(101, 160)
text.write("Magazines", align='center', font=('Times New Roman', 7, 'bold'))

# makes conveyor belt
def conveyor_belt():
	t.fillcolor(60,60,60)
	t.goto(20,-200)
	t.left(180)
	t.begin_fill()
	t.pendown()
	t.forward(40)
	t.right(90)
	t.forward(230)
	t.left(90)
	t.forward(100)
	t.right(90)
	t.forward(90)
	t.right(90)
	t.forward(40)
	t.right(90)
	t.forward(50)
	t.left(90)
	t.forward(60)
	t.left(90)
	t.forward(50)
	t.right(90)
	t.forward(40)
	t.right(90)
	t.forward(50)
	t.left(90)
	t.forward(60)
	t.left(90)
	t.forward(50)
	t.right(90)
	t.forward(40)
	t.right(90)
	t.forward(90)
	t.right(90)
	t.forward(100)
	t.left(90)
	t.forward(230)
	t.penup()
	t.end_fill()

# creates turtle for white lines
line = turtle.Turtle()
line.penup()
line.pencolor('white')
line.hideturtle()

# creates function to make lines on belt
def lines():
	# vertical lines for left
	x = -120
	y = 40
	while y <= 115:
		line.goto(x,y)
		line.pendown()
		line.forward(40)
		line.penup()
		y += 10
	# horizontal lines for left side
	x = -80
	y = 30
	line.left(90)
	while x <= -20:
		line.goto(x,y)
		line.pendown()
		line.forward(40)
		line.penup()
		x += 10
	# middle lines
	x = -20
	y = -190
	line.right(90)
	while y <= 115:
		line.goto(x,y)
		line.pendown()
		line.forward(40)
		line.penup()
		y += 10
	# vertical lines for right side
	x = 20
	y = 30
	line.left(90)
	while x <= 80:
		line.goto(x,y)
		line.pendown()
		line.forward(40)
		line.penup()
		x += 10
	# horizontal lines for right side
	x = 80
	y = 40
	line.right(90)
	while y <= 115:
		line.goto(x,y)
		line.pendown()
		line.forward(40)
		line.penup()
		y += 10
	
# calls functions
conveyor_belt()
lines()

# creates turtle for book
book = turtle.Turtle()
book.shape('book.gif')
book.penup()
book.hideturtle()
book.goto(0, -200)
book.speed(10)

#creates turtle for dvd
dvd = turtle.Turtle()
dvd.shape('dvd.gif')
dvd.penup()
dvd.hideturtle()
dvd.goto(0, -200)

# creates turtle for magazine
magazine = turtle.Turtle()
magazine.shape('magazine.gif')
magazine.penup()
magazine.hideturtle()
magazine.goto(0, -200)

# creates a box for the 'sensor'
t.fillcolor(200,164,96)
t.goto(-160, -60)
for i in range (2):
	t.begin_fill()
	t.pendown()
	t.forward(50)
	t.left(90)
	t.forward(320)
	t.left(90)
	t.penup()
	t.end_fill()

# creates a turtle to display sensor text
sensor = turtle.Turtle()
sensor.penup()
sensor.pencolor('black')
sensor.hideturtle()

# function to display a random line from books.txt
def read_book():
	sensor.clear()
	file = open("books.txt")
	list = file.readlines()
	file.close()
	# make new empty list
	make_list = []
	for i in list:
			make_list.append(i)
	sensor.goto(0, -85)
	sensor.write('Book', align='center', font=('Times New Roman', 10, 'bold'))
	sensor.goto(0, -110)
	sensor.write(random.choice(make_list), align='center', font=('Times New Roman',7,'normal'))

# function to display a random dvd from dvds.txt
def read_dvd():
	sensor.clear()
	file = open("dvds.txt")
	list = file.readlines()
	file.close()
	# make new empty list
	make_list = []
	for i in list:
			make_list.append(i)
	sensor.goto(0, -85)
	sensor.write('DVD', align='center', font=('Times New Roman', 9, 'bold'))
	sensor.goto(0, -110)
	sensor.write(random.choice(make_list), align='center', font=('Times New Roman', 7, 'normal'))

# function to display a random magazine from magazines.txt
def read_magazine():
	sensor.clear()
	file = open("magazines.txt")
	list = file.readlines()
	file.close()
	# make new empty list
	make_list = []
	for i in list:
			make_list.append(i)
	sensor.goto(0, -85)
	sensor.write('Magazine', align='center', font=('Times New Roman', 9, 'bold'))
	sensor.goto(0, -110)
	sensor.write(random.choice(make_list), align='center', font=('Times New Roman', 7, 'normal'))

# after 100 items go through, the loop stops
for i in range (100):
	item = random.randint(1,3)
	# if book, go to the left box
	if item == 1:
		book.goto(0,-200)
		book.showturtle()
		book.speed(1)
		book.goto(0,1)
		# calls function after passing through sensor
		read_book()
		book.goto(0,50)
		book.goto(-95,50)
		book.goto(-95,150)
		book.hideturtle()
	# if dvd, go to the middle box
	elif item == 2:
		dvd.goto(0,-200)
		dvd.showturtle()
		dvd.speed(1)
		dvd.goto(0,1)
		# calls function after passing through sensor
		read_dvd()
		dvd.goto(0,150)
		dvd.hideturtle()
	# if magazine, go to the right box
	elif item == 3:
		magazine.goto(0,-200)
		magazine.showturtle()
		magazine.speed(1)
		magazine.goto(0,1)
		# calls function after passing through sensor
		read_magazine()
		magazine.goto(0,50)
		magazine.goto(95,50)
		magazine.goto(95,150)
		magazine.hideturtle()
	
turtle.mainloop()