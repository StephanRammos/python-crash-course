#6-08.py
pets = []
pet = {'type': 'dog', 'owner':'Gina'}
pets.append(pet)
print(pets)
pet = {'type': 'cat', 'owner': 'Chrissy'}
pets.append(pet)
print(pets)

for pet in pets:
	print(f"This pet is a {pet['type']} and it belongs to {pet['owner']}.")