#6-03.py
glossary = {'string':'Anything inside quotes','range function':'Makes it easy to generate a series of numbers',
'list':'mutable and uses brackets','tuple': 'immutable and uses parentheses',
'conditional test' : 'is a comparison between values that results in either True or False'
}

print(glossary)

word = 'string'
print(f"\n{word} \n\t {glossary[word]}" )

word = 'range function'
print(f"\n{word} \n\t {glossary[word]}")

word = 'list'
print(f"\n{word} \n\t {glossary[word]}")
