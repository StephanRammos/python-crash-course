#6-02.py
#print key,values pairs of a dictionary
fav_nums = {
	'John': 5,
	'Mary': 7,
	'Joseph': 11,
	'Kira': 22,
	'Steven': 101
}

num = fav_nums['John']
print(f"Mandy's favorite number is {num}\n")

for name, number in fav_nums.items():
	print(f"{name}'s favorite number is {number}. ")

	
