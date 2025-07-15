#6-11.py
#a dictionary in a dictionary. Indexing a dictionary.
cities = {
	'NYC': {'country': 'USA','population': 8_000_000, 'nickname': 'the city that never sleeps'},
	'Portland': {'country': 'USA', 'population': 630_000, 'nickname': 'the City of Roses'},
	'Athens': {'country': 'Greece', 'population': 650_000, 'nickname': 'the City of Wisdom'}
}

for key, values in cities.items():
	print(cities.items())
	print(f"the city of {key}")
	print(f"\tcountry: {values['country']}")
	print(f"\tpopulation: {values['population']:,}") # format with comma using f string
	print(f"\tnickname: {values['nickname']}")