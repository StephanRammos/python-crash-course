#5-08.py
usernames = ['admin', 'a1', 'b1', 'c1', 'd1']
for username in usernames:
	if username == 'admin':
		print("Hello admin, would you like to see a status report")
	else:
		print(f"Hello, {username} thank you for logging in.")