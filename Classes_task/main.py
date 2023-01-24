from datetime import date

class User:
    def __init__(self, id, username, cr_time, storage):
        self.id = id
        self.storage = storage
        self.username = username
        self.cr_time = str(datetime.now().strftime('%D.%M.%Y'))
        
    def set_id(self, id):
        self.id = id
    
    def add_user(username):
        storage.add_user(User(username = username, cr_time = datetime.now().strftime('%D.%M.%Y')))
        
class UserStorage:
    id_generator = 1
    def __init__(self):
        self.__RECORDS = {}
        
    def get_user(self, id):
        return self.__RECORDS.get(id, None)
        
    def add_user(self, user):
        gloal id_generator
        user.set_id(id_generator)
        self.__RECORDS[id_generator] = user
        id_generator += 1 
        return user.id

storage = Storage()
user_storage = UserStorage()

class Chat:
    def __init__(self, id, name, users, cr_time, storage):
        self.id = id
        self.storage = storage
        self.name = name
        self.users = users
        self.cr_time = cr_time
         self.list_chats = []
        
    def add_chat(name, users):
        storage.add_chat(Chat(name = name, users = users, cr_time = datetime.now().strftime('%D.%M.%Y')))


class ChatStorage:
    c_id_generator = 1
    def __init__(self):
        self.__RECORDS = {}
        
    def get_chat(self, id):
        return self.__RECORDS.get(id, None)
        
    def add_chat(self, chat):
        global c_id_generator
        chat.set_id(id_generator)
        self.__RECORDS[id_generator]= chat
        c_id_generator += 1
        for user in chat.users:
            user_storage.get_user(user).add_chat(chat)
        return chat.id
        
chat_storage = ChatStorage()
        
class Message:
    m_id_generator = 1
    def __init__(self, id, chat_id, user_id, text, cr_time):
        self.id = id
        self.chat_id = chat_id
        self.user_id = user_id
        self.text = text
        self.cr_time = cr_time
        self.list_messages = []
        
    def add_message(self, message):
        self.list_messages.append(message)
        
    def add_message(self, message):
        global m_id_generator
        m_id_generator += 1 
        message.set_id(m_id_generator)
        self.__RECORDS[m_id_generator] = message
        user = message.user_id
        chat = message.chat_id
        user_storage.get_user(user).add_message(message)
        chat_storage.get_chat(chat).add_message(message)
        return message.id
    
    
class MessageStorage:
    m_id_generator = 1
    def __init__(self):
        self.__RECORDS = {}
        
    def get_message(self, id):
        return self.__RECORDS.get(id, None)
    
    def add_message(self, message):
        global m_id_generator
        m_id_generator += 1 
        message.set_id(m_id_generator)
        self.__RECORDS[m_id_generator] = message
        self.__RECORDS[message.id] = message
        m_id_generator += 1
        
message_storage = Message()
        
        
def add_user(username):
    user = User(username)
    return(user_storage.add_user(user))

def add_chat(name, users):
    chat = Chat(name, users)
    return(chat_storage.add_chat(chat))
        
def add_message(chat_id, user_id, text):
    add_message = Message(chat_id, user_id, text)
    return(message_storage.add_message(add_message))   
