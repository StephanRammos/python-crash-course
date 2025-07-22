#pizza146.py
# def make_pizza(*toppings):
# 	"""For loop to print each topping line by line"""
# 	print(f"\nMake a pizza with following toppings")
# 	for topping in toppings:
# 		print(f"- {topping}")

# make_pizza('pepperoni', 'chicken')

# def make_pizza(size,*toppings):
# 	print(f"\nMaking a {size} inch pizza with {toppings}")
# 	for topping in toppings:
# 		print(f"-{topping}")
# make_pizza(8,'pepperoni', 'chicken')

def build_profile(first, last, **user_info):
	user_info['first_name'] = first
	user_info['last_name'] = last
	return user_info

user_profile = build_profile('albert', 'einstein', location ='princeton')
print(type(user_profile))