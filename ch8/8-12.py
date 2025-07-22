#8-12.py

def print_toppings(*args):
	for arg in args:
		print(f"We are adding {arg} to your sandwich")

#call function
print_toppings('kale', 'tomatoes', 'ketchup')

