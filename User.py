class UserError(Exception):
    def __init__(self, string_error):
        self.str_err = string_error

class User:
    
    def __init__(self):
        self.db = dict()
        self.keys = tuple(self.db.keys())
        
    def add_preference(self, key, value):
        self.db[key] = value
        self.keys = tuple(self.db.keys())