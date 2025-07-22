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


#create instance of class
John = User('John','Doe',45,'TX')

#call describe_user
John.describe_user()

