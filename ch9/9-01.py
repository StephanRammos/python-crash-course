#9-01.py
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

#make instance of restaurant
my_restaurant = Restaurant('Tempe bistro', 'New American')
#print attribute restaurant_name
print(f"Restaurant name is {my_restaurant.restaurant_name}.")
print(f"We proudly serve {my_restaurant.cuisine_type}.")

print()
#calling methods
my_restaurant.describe_restaurant()
my_restaurant.open_restaurant()
