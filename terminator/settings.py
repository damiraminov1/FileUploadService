import os

import cherrypy
from dotenv import load_dotenv, find_dotenv

load_dotenv(find_dotenv('.env', raise_error_if_not_found=True))

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

TEMPLATES_PATH = os.path.join(BASE_DIR, 'terminator/templates')

# RUNNING SETTINGS
RUN_ENV = os.environ.get('RUN_ENV')

if RUN_ENV == 'development':
    GLOBAL_CONF = 'config/dev.ini'
elif RUN_ENV == 'production':
    GLOBAL_CONF = 'config/prod.ini'
else:
    raise NameError('Environment variable `RUN_ENV` is incorrect')


# APP SETTINGS

APP_CONFIG = {
    '/': {
        'tools.sessions.on': True,
        'tools.auth.on': True,
        'tools.staticdir.root': os.path.join(BASE_DIR, 'terminator'),
    },
    '/static': {
        'tools.staticdir.on': True,
        'tools.staticdir.dir': 'static',
        "tools.sessions.on": False,
        "tools.auth.on": False,
    },
}
