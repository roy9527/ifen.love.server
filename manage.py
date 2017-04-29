#!/usr/bin/env python
import os
# import sqlite3
from app import create_app, db
# from app.model import User

from flask_script import Manager, Server, Shell
from flask_cors import *

app = create_app('default')
manager = Manager(app)

CORS(app, supports_credentials=True)

@manager.shell
def make_shell_context():
    return dict(app=app, db=db)

manager.add_command("runserver", Server(
    use_debugger = True,
    use_reloader = True,
    host = '127.0.0.1')
)
manager.add_command('shell', Shell(make_context=make_shell_context))

from app.mongo_models import *

@manager.command
def make_test_data():
    words = Words(
        words_id = 1,
        words_list = [
            {"name":"abstain", "mean":"v.戒掉(烟\酒等)；避开；弃权","error_count":0,"forget_count":0, "symbol":""},
            {"name":"deck", "mean":"n.神话；虚构的信念(或观念、理论)；杜撰出来的人(或事物)","error_count":0,"forget_count":0, "symbol":""},
            {"name":"regular", "mean":"n.常客；正式队员 adj.有规律的；匀称的","error_count":0,"forget_count":0, "symbol":""},
            {"name":"abdomen", "mean":"n.腹，腹部","error_count":0,"forget_count":0, "symbol":""},
            {"name":"retain", "mean":"v.保持，保留，保存","error_count":0,"forget_count":0, "symbol":""},
            {"name":"pace", "mean":"n.步，步伐 v.踱步","error_count":0,"forget_count":0, "symbol":""},
            {"name":"abide", "mean":"v.坚持；遵守；忍受，容忍","error_count":0,"forget_count":0, "symbol":""},
            {"name":"breeze", "mean":"n.微风；轻风","error_count":0,"forget_count":0, "symbol":""},
            {"name":"diverse", "mean":"adj.不同的，差异的","error_count":0,"forget_count":0, "symbol":""},
            {"name":"horizon", "mean":"n.地平线；眼界，见识","error_count":0,"forget_count":0, "symbol":""},
            {"name":"territory", "mean":"n.地区，领土；（美国）准州；（加拿大）地方；（澳大利亚）区","error_count":0,"forget_count":0, "symbol":""},
            {"name":"abound", "mean":"v富于；充满","error_count":0,"forget_count":0, "symbol":""},
            {"name":"charm", "mean":"n.魅力，符咒 v.迷住，吸引","error_count":0,"forget_count":0, "symbol":""},
        ]
    )
    words1 = Words(
        words_id = 2,
        words_list = [
            {"name":"abstain", "mean":"v.戒掉(烟\酒等)；避开；弃权","error_count":0,"forget_count":0, "symbol":""},
            {"name":"deck", "mean":"n.神话；虚构的信念(或观念、理论)；杜撰出来的人(或事物)","error_count":0,"forget_count":0, "symbol":""},
            {"name":"regular", "mean":"n.常客；正式队员 adj.有规律的；匀称的","error_count":0,"forget_count":0, "symbol":""},
            {"name":"abdomen", "mean":"n.腹，腹部","error_count":0,"forget_count":0, "symbol":""},
            {"name":"retain", "mean":"v.保持，保留，保存","error_count":0,"forget_count":0, "symbol":""},
            {"name":"pace", "mean":"n.步，步伐 v.踱步","error_count":0,"forget_count":0, "symbol":""},
            {"name":"abide", "mean":"v.坚持；遵守；忍受，容忍","error_count":0,"forget_count":0, "symbol":""},
            {"name":"breeze", "mean":"n.微风；轻风","error_count":0,"forget_count":0, "symbol":""},
            {"name":"diverse", "mean":"adj.不同的，差异的","error_count":0,"forget_count":0, "symbol":""},
            {"name":"horizon", "mean":"n.地平线；眼界，见识","error_count":0,"forget_count":0, "symbol":""},
            {"name":"territory", "mean":"n.地区，领土；（美国）准州；（加拿大）地方；（澳大利亚）区","error_count":0,"forget_count":0, "symbol":""},
            {"name":"abound", "mean":"v富于；充满","error_count":0,"forget_count":0, "symbol":""},
            {"name":"charm", "mean":"n.魅力，符咒 v.迷住，吸引","error_count":0,"forget_count":0, "symbol":""},
        ]
    )
    words.save()
    words1.save()

@manager.command
def get_last_quiz():
    quiz_ids = Words.objects().order_by('words_id')
    quiz_idss = list(quiz_ids)
    print(quiz_idss[-1].words_id)

if __name__ == '__main__':
    manager.run()


