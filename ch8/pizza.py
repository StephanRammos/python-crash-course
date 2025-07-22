#pizza.py
# def make_pizza(size, *toppings):
# 	"""Print the list of toppings that have been requested"""
# 	print(f"make a {size} inch pizza with {toppings}")

# make_pizza(10,'pepperoni','mushrooms')

# with a for loop to print line by line
def make_pizza(size, *toppings):
	"""Print size with general message, next line use a for loop to print toppings
	line by line"""
	print(f"\nA {size} inch pizza with toppings:")
	for topping in toppings:
		print(f"-{topping}")

# (imported into making_pizza, so remove call) make_pizza(12, 'barbeque chicken', 'broccoli')

