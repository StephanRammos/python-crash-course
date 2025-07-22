#9-06.py  uses 9-01.py
class Restaurant:
	"""model a restaurant"""
	def __init__(self,restaurant_name, cuisine_type):
		"""Initialize restaurant_name and cuisine_type"""
		self.restaurant_name = restaurant_name
		self.cuisine_type = cuisine_type

	def describe_restaurant(self): # no new parameters - so just (self)
		print(f"name: {self.restaurant_name}, type: {self.cuisine_type}")

	def open_restaurant(self):
		print(f"The {self.restaurant_name.title()} is open for business.")

# #make instance of restaurant
# my_restaurant = Restaurant('Tempe bistro', 'New American')
# #print attribute restaurant_name
# print(f"Restaurant name is {my_restaurant.restaurant_name}.")
# print(f"We proudly serve {my_restaurant.cuisine_type}.")

# print()
# #calling methods
# my_restaurant.describe_restaurant()
# my_restaurant.open_restaurant()

"""
Add an attribute called flavors that 
stores a list of ice cream flavors. Write a method that displays these flavors. 
Create an instance of IceCreamStand, and call this method
"""
class IceCreamStand(Restaurant):
	"""Inherits from Restaurant class"""

	def __init__(self,restaurant_name, cuisine_type='ice cream'):
		"""Initialize attributes of the parent class"""
		super().__init__(restaurant_name, cuisine_type)
		self.flavors = []

	def display_flavors(self):
		print("We are serving flavors: ")
		for flavor in self.flavors:
			print(f" - {flavor}")

#make instance of IceCreamStand Class with same attributes as Restaurant
my_IceCreamStand = IceCreamStand("ice cream superb")
my_IceCreamStand.describe_restaurant() #print is in function do not put here or will see 'None' below output

my_IceCreamStand.flavors = ['vanilla','chocolate', 'pistachio']

#call display_flavors
my_IceCreamStand.display_flavors()

# flavors = ['chocolate', 'pistachio']
# print(f"we are serving {flavors}")