from . import api
from .. import db
import json
from flask import jsonify, request
from ..mongo_models import *

@api.route('/get_quiz_list', methods=['GET', 'POST'])
def index():
    # words = Quiz.objects.all()
    # data = jsonify(words)

    # if data:
    #     resp = make_response(data)
    # else:
    #     resp = make_response("[]")
    # resp.headers['Access-Control-Allow-Origin'] = '*'
    # return resp

    words = Quiz.objects.all()
    # for q in words.
    data = jsonify(words)
    # resp = make_response(data)
    # resp.headers['Access-Control-Allow-Origin'] = '*'
    if data:
        return data
    else:
        return '[]'

@api.route('/get_last_quiz', methods=['GET', 'POST'])
def get_word_info():
    try:
        quiz_ids = Quiz.objects().order_by('quiz_id')
        data1 = jsonify(list(quiz_ids)[-1])
        return data1
    except:
        return "[]"

@api.route('/submit_quiz', methods=['POST'])
def submit_quiz():
    data = request.get_json()
    user_id = data["user_id"]
    print(data)
    quiz_id = data["quiz_id"]
    print(quiz_id)
    error_words = data["error_words"]
    print(error_words)
    quiz_score = data['score']
    
    try:
        bill = Billing.objects.get(quiz_id=quiz_id,user_id = '9527')
        bill.score = quiz_score
        bill.update()
    except:
        Billing(
            score = quiz_score,
            quiz_id = quiz_id,
            user_id = "9527",
            is_completed = True,
        ).save()

    try:
        _quiz = Quiz.objects.get(quiz_id=quiz_id, user_id = '9527')
        length = len(_quiz.words_list)
        for i in range(0, length):
            old = _quiz.words_list[i]
            if old.name in error_words:
                old.error_count += 1
            else:
                pass
        _quiz.save()
    except:
        pass
    
    return "{\"r\":\"success\"}"