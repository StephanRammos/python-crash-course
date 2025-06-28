#3-08.py  8 travel locations
locations = ['Niihau', 'Kauai', 'Oahu', 'Molokai', 'Lanai', 'Kahoolawe', 'Maui', 'Hawaii']	
# .sort method returns None bc it overwrites the original list, unlike the sorted() function which returns a new list leaving original unchanged

print(sorted(locations))
#sh ow original list is unchanged 
print(locations)
#Use sorted() to print your list in reverse alphabetical order
print(sorted(locations, reverse = 'True'))

