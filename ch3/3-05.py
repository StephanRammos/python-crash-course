#print cancelled guest
guests = ['Chris', 'Kelsea', 'Kayley']
cancelled = 'Chris'
print(f"Unfortunately {cancelled} will not be able to attend.")

#modify list to replace Chris with new guest Danica
guests[0] = 'Danica'
print(guests)

#Print an updated invitation message for each guest
for i in range(0, len(guests)):
	print(f"{guests[i]}'s majestic presence has been requested at this exclusive dinner party\n"
		"Please reply by August 1st "

		)