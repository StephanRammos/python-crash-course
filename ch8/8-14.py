#8-14.py
#optional offroad pkg
def build_car(manufacturer, model, offroad_pkg = None, **car_info):
	""" build a dictionary containing 4 things we know about car."""
	car_info['manufacturer'] = manufacturer
	car_info['model'] = model
	if offroad_pkg:
		car_info['offroad_pkg'] = True
	#return the dictionary to fuction call
	return car_info

car_profile = build_car('honda', 'pilot', epa = 18, warranty = 5, offroad_pkg = True)
print(car_profile)