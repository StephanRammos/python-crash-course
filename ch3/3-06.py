#More guests
guests = ['Danica', 'Kaylee', 'Kelsea']
for i in range(0, len(guests)):
	print(f"Dear {guests[i]} I have been gifted a most magnificent table and can now accommodate 3 more fabulous guests")
guests.insert(0,'Sydney')
print(guests)
guests.insert(3,'Stella')
print(guests)
guests.append('Mo')
print(guests)
print("----------||||||||||||||||------------")
#print new invitation for each person in the list
for i in range(0, len(guests)):
	print(f"Dear {guests[i]} , you have been invited to a champagne dinner party.\n"
		"\t\t~~\tWe hope to see soon\t~~")

