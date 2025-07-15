#6-08.py
#append is a list method
#create dictionaries with pet info and store these dics in a list called pets.
pets = []
pet = {'type': 'dog', 'owner':'Gina'}
pets.append(pet)
print(pets)
pet = {'type': 'cat', 'owner': 'Chrissy'}
pets.append(pet)
print(pets)

for pet in pets:
	#printing elements of each dictionary respectively
	print(f"This pet is a {pet['type']} and it belongs to {pet['owner']}.")