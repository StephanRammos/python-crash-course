#8-01.py
#used f-string in body of function to print a multi line message
def display_message():
	parameter = 'Parameter is provided in the function definition.'
	argument = 'Argument is provided in the function call'
	#message = "In this Functions chapter we learned:" 
	#message += "\nthat the variable name in the definiton of function is called a parameter."
	print(f"In this functions chapter we learned\n{parameter}\n{argument}")
display_message()