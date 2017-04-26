from . import api

@api.app_errorhandler(404)
def page_not_found(errors):
    return 'api 404'

@api.app_errorhandler(500)
def internal_server_error(errors):
    return 'api 500'