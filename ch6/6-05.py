#6-05.py
rivers = {'nile':'egypt', 'salt river': 'usa','rhine': 'germany'}
for key, value in rivers.items():
	print(f"The {key.title()} runs through {value.title()}")
print()
#use a for loop to print the keys only
for key in rivers.keys():
	print(f"{key.title()}")
#use a for loop to print the values only
print()
for value in rivers.values():
	print(f"{value.title()}")