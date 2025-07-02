#5-11.py
#use a for loop to populate a list containing [1,2,3,4,5,6,7,8,9] : use .append() method
numbers = []
for i in range(3,10):
	numbers.append(i)
print(numbers)

#loop through list, print ordinal index of each element in the list
# Tuple unpacking in Python is a feature that allows the elements of a 
#tuple (or any iterable) to be assigned to individual variables in a single assignment statement.
"""
The for loop iterates over each element in the list. As it iterates, enumerate takes each element, 
one element at a time and generates an (index, value) pair. This is syntactically 
represented by the comma: idx, num . This is together called tuple (any iterable-list,etc) unpacking.
"""
for index, number in enumerate(numbers, start = 1):
	#Different ordinal suffixes for 1,2,3.
	if index == 1:
		suffix = "st"
	elif index == 2:
		suffix = "nd"
	elif index == 3:
		suffix = "rd"
	else:
		suffix = "th"
	print(f"{number} is the {index}{suffix} element in the list")