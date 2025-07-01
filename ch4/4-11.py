#4-11.py	 Use list in 4-01.py 

pizzas = ['Hawaiian', 'Sicilian', 'White cheese']
friends_pizzas = pizzas[:]
print(friends_pizzas)

# Use a for loop ot print my fav pizzas each on a seperate line
print('My fav pizzas are:')
for pizza in pizzas:
	print(pizza)

friends_pizzas.append('Feta')
print(friends_pizzas)

print("my friends fav pizzas are: ")
for friends_pizza in friends_pizzas:
	print(friends_pizza)
