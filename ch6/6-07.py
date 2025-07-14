#6-07.py uses 6-01.py
# print each data value on a seperate line using a seperate print(stmt) ie hard coding
people = [] # intialize empty list
person = {'first_name': 'Stephan', 'last_name': 'Roberts', 'age': 35, 'city': 'Phoenix'}
people.append(person)
print(people)
person = {'first_name':'Sam', 'last_name': "Pappis", 'age':40, 'city': 'NYC'}
people.append(person)
person = {'first_name': 'Mary', 'last_name': 'Schwartz', 'age' :60 , 'city': 'Munich'} 
people.append(person)


for person in people:
	print(f"{person['first_name']} {person['last_name']} is {person['age']} years old and is from {person['city']}.")