#4-13.py
buffet_foods = ('chicken marsala', 'pallela', 'shrimp linguine') 
for buffet_food in buffet_foods:
	print(buffet_food)

#attempt to modify tuple at index 0 , to show immutability of tuple
#python output: TypeError: 'tuple' object does not support item assignment
#buffet_foods[0]= 'steak'

print('--------------\n')

#rewrite the entire tuple (all elements) to change 2 of the meals
buffet_foods = ('steak', 'pallela', 'bass with pasta')
for buffet_food in buffet_foods:
	print(buffet_food)