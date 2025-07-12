#6-04.py
#use the dictionary method .items()
glossary = {'string':'Anything inside quotes','range function':'Makes it easy to generate a series of numbers',
'list':'mutable and uses brackets','tuple': 'immutable and uses parentheses',
'conditional test' : 'is a comparison between values that results in either True or False'
}

for key, value in glossary.items():
	print(f"\n{key}\n\t {value}")
