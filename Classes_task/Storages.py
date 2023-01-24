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
