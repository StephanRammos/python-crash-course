#6-10.py uses 6-02.py p.99
#each key can have several values
fav_nums = {
	'John': [5,10,15],
	'Mary': [7,14,21],
	'Joseph': [11,22,33],
	'Kira': [22,44,66],
	'Steven': [101,202]
}

for key , values in fav_nums.items():
	print(f"\n{key}'s favorite number is :")
	for value in values:
		print(value)