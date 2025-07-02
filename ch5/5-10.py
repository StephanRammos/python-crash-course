#5-10.py
current_users = ['A1', 'B1', 'C1', 'd1', 'e1']
new_users = ['a1', 'b1', 'm1', 'n1', 'p1']
current_users_lower = []
#append lowercase elements of current_users to the empty list above
for current_user in current_users:
	current_users_lower.append(current_user.lower())
print(current_users_lower)

for new_user in new_users:
	if new_user in current_users_lower:
		print("Sorry, you will have to enter a different user name")