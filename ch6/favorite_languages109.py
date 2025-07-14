favorite_languages = {
	'jen': ['python', 'ruby'],
	'sarah': ['c']
}
print(favorite_languages.items())
list1 = []  #same elements as list languages
for name, languages in favorite_languages.items():
	if len(languages) > 1:
		print(f"{name.title()}'s favorite languages are:")
	else:
		print(f"{name.title()}'s fav language is: ")
	for language in languages:
		list1.append(language) #languages plural will look just like list1 at each iteration
		print(f"\t{language.title()}")
	print(list1)