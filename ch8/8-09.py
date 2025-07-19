#8-09.py
text_messages = ['Hi, how was your day?', "Did you hear the news?", "When is her birthday?"]
print(text_messages.pop())
def show_messages(text_messages):
	for text_message in text_messages:
		print(text_message)

show_messages(text_messages)
