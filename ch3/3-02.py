#one line print statements
#Best practices: use a plural name for list helpful for looping
names = ['Eric', 'Kevin', 'James', 'Bill']
# print(f"{names[0].title()}")

# print (f"{names[1].title()}")

# print( f"{names[2].title()}")

# use a for loop with python taking care of the number of loops
# for name in names:
# 	print(name)

# use len function to determine upper limit of for loop
#recall in python , the range(start,stop) function includes the start but not the stop(not 4 here).
for i in range (0, len(names)):
	print(names[i])

