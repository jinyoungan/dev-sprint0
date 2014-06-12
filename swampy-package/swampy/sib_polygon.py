# Polygon excercise from Week 0

# Name: JIN YOUNG AN


from TurtleWorld import * 		
world = TurtleWorld()			
bob = Turtle()				



# This is where you put code to move bob

def square(turtle, length):
	for i in range(4):
		fd(turtle, length)
		lt(turtle)
print square(bob, 100)

def polygon(turtle, n, length):
	angle = 360/n
	for i in range(n):
		fd(turtle, length)
		lt(turtle, angle)

def circle(turtle, radius):
	



wait_for_user()					
