#9-07.py
#9-03.py
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
		self.privileges = [] #the privileges list is created inside the Admin class.

	def show_privileges(self):
		print("\nThe admin has the following privileges:")
		for privilege in self.privileges:
			print(f"-{privilege}")

#create instance of class
#John = User('John','Doe',45,'TX')
#create instance of Admin (child) class
Mary = Admin('Mary', 'Paper', 50, 'NV')
#call describe_user
#John.describe_user()
Mary.describe_user()
#call greet_user()
#John.greet_user()
#build the privileges list for Admin Mary
Mary.privileges = ["can add post", "can delete post", "can ban user"]


#call show_privileges
Mary.show_privileges() #method is in the Admin class
