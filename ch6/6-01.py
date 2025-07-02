# 6-01.py 
# print each dat value on a seperate line using a seperate print(stmt) ie hard coding
person = {'first_name': 'Stephan', 'last_name': 'Roberts', 'age': 35, 'city': 'Phoenix'}
print(person['first_name'])
print(person['last_name'])
print(person['age'])
print(person['city'])

print('\n')
#print each value using for loop and the dict method .values()
for value in person.values():
	print(value)