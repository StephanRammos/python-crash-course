#8-04.py
def make_shirts(graphic= 'I love Python', size= 'large'):
	print(f"Size is {size}\nGraphic: {graphic}")

#call with no arguments to get default message and size
make_shirts()

#call with size argument = medium, default message
make_shirts(size = 'medium')

# call size small, with diferent message
make_shirts(size = 'small', graphic = "I love Java")
