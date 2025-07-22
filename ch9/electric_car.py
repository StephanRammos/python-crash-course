#electric_car.py  inherits from car.py
#car.py
#output: 2024 Audi A4
class Car:
	"""A simple attempt to represent a car"""
	def __init__(self, make, model, year): #odometer_reading is not in parameters, so we will need a function to change its value.
		"""Initialize attributes to describe a car"""
		self.make = make
		self.model = model
		self.year = year
		self.odometer_reading = 0

	def get_descriptive_name(self):
		"""Return a neatly formatted descriptive name"""
		long_name = f"{self.year} {self.make} {self.model}"
		return long_name.title()

	def read_odometer(self):
		"""Print a statement showing the car's mileage"""
		print(f"This car has {self.odometer_reading} miles on it")
		

	def update_odometer(self, mileage):
		"""Set the odometer to the given value. Reject the change if it attempts to roll back the odometer."""
		self.odometer_reading = mileage
		if mileage >= self.odometer_reading:
			odometer_reading = mileage
		else:
			print("You can't roll back the odometer")

	def increment_odometer(self, miles):
		"""Add the given amount to the odometer"""
		self.odometer_reading += miles

my_used_car = Car('nissan','armada', 2020) #Create instance of Car
print(my_used_car.get_descriptive_name()) #print stmt on the result of a function call

my_used_car.update_odometer(23_500)
my_used_car.read_odometer()

my_used_car.increment_odometer(100)
my_used_car.read_odometer()

# my_new_car = Car('audi','a4',2024) #Create a 2nd instance of Car
# print(my_new_car.get_descriptive_name())

# my_new_car.odometer_reading = 23 #Directly modify attributes value through an instance.
# print(my_new_car.read_odometer())

# my_new_car.update_odometer(300)
# print(my_new_car.read_odometer())

class ElectricCar(Car):

	def __init__(self, make, model, year):
		"""Initialize attributes of the parent class"""
		super().__init__(make, model, year)
		self.battery_size = 40

	def describe_battery(self):
		"""Print a stmt describing the battery size"""
		print(f"This car has a {self.battery_size} - kWh battery.")

my_leaf = ElectricCar('nissan', 'leaf' , 2024)
print(my_leaf.get_descriptive_name())
my_leaf.describe_battery()





