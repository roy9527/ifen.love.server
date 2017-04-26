from . import api

@api.app_errorhandler(404)
def page_not_found():
    return 'api 404'

@api.app_errorhandler(500)
def internal_server_error():
    return 'api 500'