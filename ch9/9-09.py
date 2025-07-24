#9-09.py
""" Battery Upgrade: Use the final version of electric_car.py from this section. 
Add a method to the Battery class called upgrade_battery(). This method 
should check the battery size and set the capacity to 65 if it isn’t already. Make 
an electric car with a default battery size, call get_range() once, and then 
call get_range() a second time after upgrading the battery. You should see an 
increase in the car’s range """

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


class Battery:
	"""Add Battery() Class  w default 'battery_size' of 40kw"""
	def __init__(self, battery_size=40):
		"""Initialize the battery's attribute"""
		self.battery_size = battery_size

	def describe_battery(self):
		"""Print a stmt describing the battery size"""
		print(f"This car has a {self.battery_size}-kWh battery.")

	def get_range(self):
		"""Print the range of battery based on size kWh"""
		if self.battery_size == 40:
			range = 150
		elif self.battery_size == 65:
			range = 225
		print(f"This car can go about {range} miles on a full charge.")

	def upgrade_battery(self):
		if self.battery_size == 40:
			self.battery_size = 65
			print("Upgraded battery_size to 65")
		else:
			print("The battery is already upgraded")




# my_used_car = Car('nissan','armada', 2020) #Create instance of Car
# print(my_used_car.get_descriptive_name()) #print stmt on the result of a function call

# my_used_car.update_odometer(23_500)
# my_used_car.read_odometer()

# my_used_car.increment_odometer(100)
# my_used_car.read_odometer()

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
		# self.battery_size = 40  this has been moved to  Battery()
		self.battery = Battery()
	"""Removed the describe_battery method from ElectricCar"""
	# def describe_battery(self):
	# 	"""Print a stmt describing the battery size"""
	# 	print(f"This car has a {self.battery_size} - kWh battery.")


print("make an electric car and check the range")
my_leaf = ElectricCar('nissan', 'leaf' , 2024)
my_leaf.battery.get_range()

print("Upgrade the battery and check the range again")
my_leaf.battery.upgrade_battery()
my_leaf.battery.get_range()



#my_leaf.describe_battery() --> battery is no longer a part of ElectricCar class, but of Battery class.






