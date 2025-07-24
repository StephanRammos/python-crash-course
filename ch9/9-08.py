# 9-08 has object inside object, uses 9-07
"""Privileges: Write a separate Privileges class. The class should have one 
attribute, privileges, that stores a list of strings as described in Exercise 9-7. 
Move the show_privileges() method to this class. Make a Privileges class instance 
as an attribute in the Admin class (as we did Battery class instance as an attribute in the ElectricCar class in electric_car.py.) Create a new instance of Admin and use your 
method to show its privileges. """

class User:
	"""first_name, last_name and other parameters typical for a user account
	method called describe_user() that prints user info
	"""
	def __init__(self, first_name, last_name, age, state):
		self.first_name = first_name
		self.last_name = last_name
		self.age = age
		self.state = state

	def describe_user(self):
		print(f"{self.first_name} {self.last_name} is {self.age} years old and lives in {self.state}")

	def greet_user(self):
		print(f"Welcome to the site {self.first_name}")

class Admin(User):
	"""Add an attribute, privileges, that stores a list of 
strings like "can add post", "can delete post", "can ban user" """
	def __init__(self,first_name, last_name, age, state ):
		"""Initialize attributes of the parent class"""
		super().__init__(first_name, last_name, age, state)
		#self.privileges = []
		self.privileges = Privileges() #this is an object		

class Privileges:
	def __init(self,privileges = []):
		"""Initialize the privilege's attribute"""
		self.privileges = privileges # list is wrapped in this class

	def show_privileges(self):
		print("\nThe admin has the following privileges:")
		if self.privileges:
			for privilege in self.privileges:
				print(f"-{privilege}")
		else:
			print("User has no privileges")



#create instance of class
#John = User('John','Doe',45,'TX')
#create instance of Admin (child) class
Mary = Admin('Mary', 'Paper', 50, 'NV')
#call describe_user
#John.describe_user()
Mary.describe_user()
#call greet_user()
#John.greet_user()
#print the privileges for Mary before assigning her privileges to check if..else
#Mary.privileges.show_privileges()
#build the privileges list for Admin Mary
print("adding privileges")
Mary_privileges = ["can add post", "can delete post", "can ban user"]
#bc list object we have to go one more dot level in. We go into self.privileges at the for and also in the def __init__
Mary.privileges.privileges = Mary_privileges # object.attribute name from where Mary was created (Admin class ie one level up from where method is made).method
""" Above - So we have an admin object I called Mary. So we go to the class she was created, we see 'self.privileges = Priviliges() --> our first .privileges
Then we go to the Privileges class and see 'self.privilege = privileges' --> our 2nd .priviliges

"""
#call show_privileges
Mary.privileges.show_privileges() 



