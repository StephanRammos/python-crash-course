#9-05.py uses 9-03.py
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
		self.login_attempts = 0

	def describe_user(self):
		print(f"{self.first_name} {self.last_name} is {self.age} years old and lives in {self.state}")

	def increment_login_attempts(self): #increment by 1
		self.login_attempts +=1

	def reset_login_attempts(self):
		self.login_attempts = 0


#create instance of class
John = User('John','Doe',45,'TX')

#call describe_user
#John.describe_user()

#call increment_login_attempts several times
John.increment_login_attempts()
John.increment_login_attempts()
John.increment_login_attempts()

print(John.login_attempts) # prints 3, since incremented 3 times.

#call reset
John.reset_login_attempts()

print(John.login_attempts) #prints 0, since login was reset to 0.


