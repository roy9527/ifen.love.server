from . import api
from .. import db
import json
from flask import jsonify
from ..mongo_models import *

@api.route('/get_quiz_list', methods=['GET', 'POST'])
def index():
    # words = Quizs.objects().paginate(page=1, per_page=10)
    words = Quizs.objects.all()
    # for q in words.
    if words:
        return jsonify(words)
    else:
        return '[]'

@api.route('/get_last_quiz', methods=['GET', 'POST'])
def get_word_info():
    quiz_ids = Words.objects().order_by('words_id')
    # quiz_idss = list(quiz_ids)
    return jsonify(list(quiz_ids)[-1])

@api.route('/submit_quiz', methods=['GET', 'POST'])
def submit_quiz():
    quiz = Quizs(
        score = 100,
        quiz_id = 9528,
        is_completed = True,
    )
    quiz.save()
    return 'quiz save ok.'