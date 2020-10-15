import json
file_name = 'D:\\Projects\\Insta\\venv\\src\\messages.json'

def get_conversation_with(conversations,desired_person):
    for conversation in conversations:
        participants = conversation['participants']
        if len(participants) == 2 and desired_person in participants:
            return conversation['conversation']
    raise Exception('No existing conversation' + desired_person)

def get_message(conversation):
    messages = []
    for message in conversation:
        sender = message['sender']
        text = message['text'] if 'text' in message else '<no text message>'
        str1 = sender + " : "
        str1 = str1 + str(text)
        messages.append(str1)
    return messages[::-1]

with open(file_name,encoding='utf8') as json_file:
    desired_person = '_zywoo___'
    conversations = json.load(json_file)
    conversation = get_conversation_with(conversations,desired_person)
    messages = get_message(conversation)
    for message in messages:
        print(message)