#8-10.py
messages = ['Hi, how was your day?', "Did you hear the news?", "When is her birthday?"]
sent_messages = []

#print the elements in messages  
def send_messages(messages,sent_messages):
	while len(messages) > 0:
		message = messages.pop()
		print(f"message: {message}")
		sent_messages.append(message)

# function that prints the elements in the populated list - sent_messages
def show_sent_messages(sent_messages):
	print('the following messages have been sent\n')
	for sent_message in sent_messages:
		print(f"message: {sent_message}")


#call send_messages
send_messages(messages,sent_messages)
#call show
show_sent_messages(sent_messages)
