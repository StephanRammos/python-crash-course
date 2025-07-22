#no calls here bc will import into 8-15.py
#after print each design name; pop from full list, append to empty.
unprinted_designs = ['phone case','robot pendant', 'dodecahedron']
completed_models = []

#printing_functions.py
#Version 2 - 2 user defined functions increase usability - can call function
#print the elements in unprinted line by line
def print_models(unprinted_designs, completed_models):
	while unprinted_designs:
		current_design = unprinted_designs.pop()
		print(f"{current_design}")
		completed_models.append(current_design)

#print the elements in completed line by line
def show_completed_models(completed_models):
	print('the following models have been printed:\n')
	for completed_model in completed_models:
		print(completed_model)