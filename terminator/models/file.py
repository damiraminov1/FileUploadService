import os
import shutil
import string
from datetime import datetime
from random import choices
from time import time

import cherrypy


class FileObject:
    def __init__(self, file):
        self._name = self.name(old_name=file.filename)
        self._path = self.path()
        self._url = self.url()

    def path(self) -> str:
        global DATA_PATH
        DATA_PATH = os.path.join(cherrypy.config['server_directory'], date_path())
        if not os.path.exists(DATA_PATH):
            os.makedirs(DATA_PATH)
        shutil.move(self._name, DATA_PATH)
        return DATA_PATH

    def name(self, old_name) -> str:
        file_format = '.' + str(old_name).split('.')[-1]
        new_name = str(int(time())).join(choices(string.ascii_lowercase, k=4)) + file_format
        os.rename(old_name, new_name)
        return new_name

    def url(self) -> str:
        nginx_uri: str = cherrypy.config['nginx_uri']
        result = os.path.join(nginx_uri, date_path(), self._name)
        return '<a href="{}">{}</a>'.format(result, result)


def get_correct_month() -> str:
    if datetime.today().month in [10, 11, 12]:
        return str(datetime.today().month)
    else:
        return '0' + str(datetime.today().month)


def date_path() -> str:
    return os.path.join(str(datetime.today().year), get_correct_month(), str(datetime.today().day))
