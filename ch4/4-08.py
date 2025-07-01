#4-08.py	Make a list of the cubes of each integer from 1 to 10 inclusive.
cubes = []
for i in range(1,11):
	cubes.append(i**3)

print(cubes)
print("using list comprehension below : ")
# list_name = [operation  for i in range( , )]
cubes = [i**3  for i in range(1,11)]
print(cubes)