#5-05.py
alien_color = 'yellow'
#v1 : two elif's
if alien_color == 'green':
	print("You've earned 5 points")

elif alien_color == "yellow":
	print("You've earned 10 points")

elif alien_color == 'red':
	print("You've earned 15 points")

#v2  , using else 
alien_color = 'red'

if alien_color == 'green':
	print("You've earned 5 points")

elif alien_color == "yellow":
	print("You've earned 10 points")

else:
	print("You've earned 15 points")
#v3: series of if stmts - best used when more than 1 block of code needs to run
alien_color = 'red'

if alien_color == 'green':
	print("You've earned 5 points")

if alien_color == "yellow":
	print("You've earned 10 points")

if alien_color == 'red':
	print("You've earned 15 points")
