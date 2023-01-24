from Storages import *
from main import *

def add_user(username):
    user = User(username)
    return(user_storage.add_user(user))

def add_chat(name, users):
    chat = Chat(name, users)
    return(chat_storage.add_chat(chat))
        
def add_message(chat_id, user_id, text):
    add_message = Message(chat_id, user_id, text)
    return(message_storage.add_message(add_message))   
