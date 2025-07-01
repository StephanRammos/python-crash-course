#5-06.py
age = 14
if age < 2:
	print("This person is a baby")
#used chained comparison notation
elif 2 < age < 4:
	print("This person is a toddler")
elif 4 <= age < 13 :
	print("This person is a kid")
elif 13 <= age < 20:
	print("This person is a teenager")
elif age >= 13 and age < 20:
	print("This person is an adult")
elif age >= 20 and age < 65:
	print("This person is an adult")
elif age >= 65 :
	print("This person is an elder")