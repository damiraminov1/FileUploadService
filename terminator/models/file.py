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

    def path(self):
        global DATA_PATH
        DATA_PATH = os.path.join(cherrypy.config['server_directory'],
                                 str(datetime.today().year),
                                 str(datetime.today().month),
                                 str(datetime.today().day))
        if not os.path.exists(DATA_PATH):
            os.makedirs(DATA_PATH)
        shutil.move(self._name, DATA_PATH)
        return DATA_PATH

    def name(self, old_name):
        file_format = '.' + str(old_name).split('.')[-1]
        new_name = str(int(time())).join(choices(string.ascii_lowercase, k=4)) + file_format
        os.rename((os.path.abspath(old_name)).split('/')[-1], new_name)
        return new_name
