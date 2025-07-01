#5-01.py
cars = ['audi', 'bmw', 'nissan', 'subaru', 'toyota', 'ford', 'gm']

# for car in cars:
# 	if car == 'bmw':
# 		print(car.upper())
# 	else:
# 		print(car.title())

# for car in cars:
# 	if car == 'audi' or car == 'bmw':
# 		print("This car manufacturer's headquarters are in Germany ")

# 	elif car == 'subaru' or car == 'toyota' or car == 'nissan':
# 		print("This car manufacturer's headquarters are in Japan")

# 	else : 
# 		print(f"{car}'s manufacturer's headquarters are in USA")

#convert list to proper case, or if intials then all upper
# for car in cars:
# 	if len(car) <= 3:
# 		car = car.upper() 
# 		print(car )

# 	else:
# 		car = car.title()
# 		print(car)

# test with T/F print out if car from list is made in Japan
for car in cars:
	if car == "nissan":
		print(f"{car.title()} is the best" )

#Books test
car = 'subaru'
print("Is car == 'subaru' ? I predict True." )
print(car == 'subaru')

print("\nIs car == 'audi'? I predict False.")
print(car == 'audi')

#----------
#create fruits list and non_fruits list using append
foods = ['pasta', 'steak', 'apple', 'orange']
fruits = []
non_fruits = []
for food in foods:
	if food != 'pasta' and food != 'steak' :
		fruits.append(food)
print(f"fruits are {fruits}")

for food in foods:
	if food not in fruits:
		non_fruits.append(food)
print(f"\nnon fruits are: {non_fruits}")

#store the short names(BMW, GM) in list short_names and others on list long_names
#use the for loop to build the initially empty lists
# short_names = []
# long_names = []

# for car in cars:
# 	if len(car) <= 3:
# 		short_names.append(car.upper())
# 	else:
# 		long_names.append(car.title())

# #print both groups
# for name in short_names:
# 	print(name)
# print()

# for name in long_names:
# 	print(name)