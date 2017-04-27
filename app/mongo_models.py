# from flask.ext.mongokit import Document

# class Quizs(Document):
#     __collection__ = 'quizs'
#     structure = {
#         'score': int,
#         'quiz_id': unicode,
#         'user_id':unicode,
#         'creation': datetime,
#     }
#     required_fields = ['quiz_id', 'score']
#     default_values = {'creation': datetime.utcnow()}
#     use_dot_notation = True
from datetime import datetime
from . import db

class User(db.Document):
    meta = {
        'collection': 'user',
        'ordering': ['-email'],
        'strict': False,
    }
    email = db.StringField()
    nick_name = db.StringField(max_length=50)
    avatar = db.StringField()
    pass_word = db.StringField(max_length=50)
    open_id = db.StringField()
    def to_json(self):
        return {
            'nick_name' : self.nick_name,
            'email' : self.email,
            'avatar' : self.avatar,
            'open_id' : self.open_id,
        }


class Quizs(db.Document):
    meta = {
        'collection': 'quizs',
        'ordering': ['-create_at'],
        'strict': False,
    }
    create_at = db.DateTimeField(default=datetime.now)
    is_completed = db.BooleanField(default=False)
    score = db.IntField(default=0)
    quiz_id = db.IntField(default=1)
    user = db.ReferenceField(User)
    def to_json(self):
        return {
            'is_completed' : self.is_completed,
            'score' : self.score,
            'quiz_id' : self.quiz_id,
            'user' : self.user.to_json(),
        }

class Words(db.Document):
    meta = {
        'collection': 'words',
        'ordering': ['-words_id'],
        'strict': False,
    }
    words_id = db.IntField()
    #{"name":"play", "mean":"玩","error_count":0,"forget_count":0, "symbol":""}
    words_list = db.ListField()
    # words_mean_list = db.ListField()
    # words_symbol_list = db.ListField()
    # words_erorr_list = db.ListField()
    # words_forget_list = db.ListField()
    def to_json(self):
        return {
            'words_id' : self.words_id,
        }