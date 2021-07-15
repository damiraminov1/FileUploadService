import string
from datetime import datetime
import os
import shutil
from time import time
from random import choices


DATA_PATH = ('/opt/server_data' + '/' +
             str(datetime.today().year) + '/'
             + str(datetime.today().month) + '/'
             + str(datetime.today().day))


class FileObject:
    def __init__(self, file):
        self._name = self.name(old_name=file.filename)
        self._path = self.path()


    def path(self):
        if not os.path.exists(DATA_PATH):
            os.makedirs(DATA_PATH)
        shutil.move(self._name, DATA_PATH)
        return DATA_PATH

    def name(self, old_name):
        file_format = '.' + str(old_name).split('.')[-1]
        new_name = str(int(time())).join(choices(string.ascii_lowercase, k=4)) + file_format
        os.rename((os.path.abspath(old_name)).split('/')[-1], new_name)
        return new_name
