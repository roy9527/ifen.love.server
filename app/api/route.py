from . import api

@api.route('/', methods=['GET', 'POST'])
def index():
    return 'hello api.'

@api.route('/get_word_info', methods=['GET', 'POST'])
def get_word_info():
    return 'word.'