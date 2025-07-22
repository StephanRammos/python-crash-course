#8-06.py
#formatting function expanded to include proper formatting by countries represeented by Acronym.
def city_country(city, country):
	if len(country)<4:
		full_name = f"{city.title()}, {country.upper()}"
		return full_name
	else:
		full_name = f"{city.title()}, {country.title()}"
		return full_name

#function call
full = city_country('phoenix', 'USA')
print(full)