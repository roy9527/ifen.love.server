config = {
    
}

class Config():
    def __init__(self):
        pass

class DevConfig(Config):
    debug = True
    SQLALCHEMY_DATABASE_URI = "sqlite:///database.db"