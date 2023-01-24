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
    
    
        
        
