#8-03.py
def make_shirt(size, graphic):
	print(f"size: {size.title()}\ngraphic: {graphic}")
#call using pos arg
make_shirt('medium','No Fear')
print()
#call using keyword arg
make_shirt(size= 'medium', graphic = 'No Fear')
