#dog.py
class Dog:
	""" model a dog """
	def __init__(self, name, age):
		"""Initialize name and age attributes"""
		self.name = name
		self.age = age

	def sit(self):
		"""Simulate a dog sitting in response to a command"""
		print(f"{self.name} is now sitting.")

	def roll_over(self):
		"""Simulate rolling over in response to a command"""
		print(f"{self.name} rolled over!")

#make instance of dog
my_dog = Dog('Willie',6)
#look at the instance my_dog and print the attribute name
print(f"My dog's name is {my_dog.name}.")
#look at the instance of my_dog and print the attribute age
print(f"{my_dog.name} is {my_dog.age} years old.")

#calling methods
my_dog.sit()
my_dog.roll_over()

#create a second dog instance called your_dog
your_dog = Dog('Lucy', 3)

print(f"My dog's name is {your_dog.name}.")