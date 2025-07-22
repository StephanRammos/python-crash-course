#8-13.py
#name of dictionary is 'user_info'
# a function 'build_profile' that accepts an arbitrary number of keyword args
def build_profile(first, last, **user_info):
	"""Build a dictionary containing everything we know about a user"""
	user_info['first_name'] = first
	user_info['last_name'] = last
	return user_info

user_profile = build_profile('Stephan', 'Rammos', location = 'AZ', field = 'AI', hobby = 'boating')
print(user_profile)

