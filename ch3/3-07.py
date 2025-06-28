#3-07.py
#remove people from list, until only 2 are left
guests = ['Danica', 'Kaylee', 'Kelsea', 'Sydney', 'Stella', 'Mo']
print("Shipping delay with my new table, so I can only invite 2 guests now, sorry..")

while len(guests)  > 2 :
	removed = guests.pop()
	print(f"My sincerest apologies {removed}, I will put you at the top of the list for my next invite,\n"
		"\t hope to see you at next dinner :)")


print(f"Dearest {guests[0]} and {guests[1]} you are the chosen guests, and I look forward to hosting you both for a wonderful dinner")