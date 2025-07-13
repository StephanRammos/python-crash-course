#6-06.py
favorite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'ruby',
    'phil': 'python',
    }

persons = ['phil', 'sarah', 'steve','john']

for person in persons:
	if person in favorite_languages.keys():
		print(f"Thanks for taking the poll {person.title()}")
	else:
		print(f"{person.title()}, we'd like to invite you to take the poll")

