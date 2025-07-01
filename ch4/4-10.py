#4-10.py
#use list from 4-07.py to slice
three_m = []
for i in range(1,11):
	three_m.append(3*i)

print(three_m)

print("The first three items in the list are: ")
print(three_m[0:3])

print("Three items from the middle of the list are:")
print(three_m[3:6])

print("The last 3 elements of the list are:")
print(three_m[-3:])