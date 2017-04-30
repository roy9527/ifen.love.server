from datetime import datetime
from . import db

class User(db.Document):
    meta = {
        'collection': 'user',
        'ordering': ['-user_id'],
        'strict': False,
    }
    email = db.StringField()
    nick_name = db.StringField(max_length=50)
    avatar = db.StringField()
    pass_word = db.StringField(max_length=50)
    open_id = db.StringField()
    user_id = db.StringField()
    def to_json(self):
        return {
            'nick_name' : self.nick_name,
            'email' : self.email,
            'avatar' : self.avatar,
            'open_id' : self.open_id,
            'user_id' : self.user_id,
        }


class Billing(db.Document):
    meta = {
        'collection': 'Billing',
        'ordering': ['-quiz_id'],
        'strict': False,
    }
    create_at = db.DateTimeField(default=datetime.now)
    is_completed = db.BooleanField(default=False)
    score = db.FloatField(default=0)
    quiz_id = db.IntField(default=1)
    user_id = db.StringField()
    def to_json(self):
        return {
            'is_completed' : self.is_completed,
            'score' : self.score,
            'quiz_id' : self.quiz_id,
            'user_id' : self.user_id,
        }

#{"name":"play", "mean":"玩","error_count":0,"forget_count":0, "symbol":""}
class Word(db.EmbeddedDocument):
    name = db.StringField(required=True)
    mean = db.StringField(required=True)
    symbol = db.StringField()

    error_count = db.IntField(default=0)
    forget_count = db.IntField(default=0)


class Quiz(db.Document):
    meta = {
        'collection': 'quiz',
        'ordering': ['-quiz_id'],
        'strict': False,
    }
    quiz_id = db.IntField(required=True)
    create_at = db.DateTimeField(default=datetime.now)
    words_list = db.ListField(db.EmbeddedDocumentField(Word))
    user_id = db.StringField()
    def to_json(self):
        return {
            'quiz_id' : self.quiz_id,
        }