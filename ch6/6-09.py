#6-09.py
#person's name is the dictionary key 
# do NOT make a list of dictionaries like in 6-08.py
#since the name keys are all unique, will have to use a nested for
favorite_places = {
'John': ['Mykonos', 'Santorini', 'Colorado'],
'Mike': ['Texas','Arizona','Spain'],
'Debbie': ['Montanta', 'Madrid','Oahu']
}
#loop through dictionary , printing each person's name and fav place respectively.
print(favorite_places.items())
# k, v : positional argument
for person, places in favorite_places.items(): #create a key, value pairing for each dictionary entry(3 rows).
	#print(f"{person}'s favorite places are: {places}")
	print(f"\n{person}'s favorite places are: ")
	#print the list elements for each person(key) on a seperate line
	for place in places:
		print(place)
