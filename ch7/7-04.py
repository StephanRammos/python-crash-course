#7-04.py
prompt = "\nPlease enter the topping you would like "
prompt += "\n(Enter quit when finished)\n"

while True:
	topping = input(prompt)

	if topping == 'quit':
		break
	else:
		print(f"We are adding {topping} to your pizza")