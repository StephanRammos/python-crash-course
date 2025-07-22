#9-04.py uses 9-01.py
class Restaurant:
	"""model a restaurant"""
	def __init__(self,restaurant_name, cuisine_type): #number_served is not in paramters, so we will need a function to change its value.
		"""Initialize restaurant_name and cuisine_type"""
		self.restaurant_name = restaurant_name
		self.cuisine_type = cuisine_type
		self.number_served = 1000

	def describe_restaurant(self): # no new parameters - so just (self)
		print(f"name: {self.restaurant_name}, type: {self.cuisine_type}")

	def open_restaurant(self):
		print(f"The {self.restaurant_name.title()} is open for business.")

	#create function to print the number of customers served. Similiar to read_odometer in car.py
	def read_number_served(self):
		print(f"This restaurant has served {self.number_served} over its 10 years in business")

	#create function 'increment_number_served' to represent the daily count
	def increment_number_served(self,daily_count):
		self.number_served += daily_count
		print(f"This restaurant has served {self.number_served} customers")

	#Extra: change values of variable number_served. Used if the increment function above did not work one day. 
	def update_number_served(self,latest_number_served):
		"""the latest count we have must overwrite the current value in number_served"""
		number_served = latest_number_served
		print(f"This restaurant served {number_served}")


#make instance of restaurant
# my_restaurant = Restaurant('Tempe bistro', 'New American')
# #print attribute restaurant_name
# print(f"Restaurant name is {my_restaurant.restaurant_name}.")
# print(f"We proudly serve {my_restaurant.cuisine_type}.")

# print()
# #calling methods
# my_restaurant.describe_restaurant()
# my_restaurant.open_restaurant()

#create an instance called restaurant 
restaurant = Restaurant('Beach Diner', 'bar food')
#print the number of customers served
restaurant.read_number_served()
#print the latest number
restaurant.update_number_served(14)

#call the increment_number_served function to add the day's customer count to total life of business count
restaurant.increment_number_served(10)


