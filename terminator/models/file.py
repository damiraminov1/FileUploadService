import os
import string
from datetime import datetime
from random import choices
from pathlib import Path

import cherrypy


class FileObject:
    def __init__(self, raw_data, filename):
        self._created_at: datetime = datetime.now()
        self.name = filename
        self._data = raw_data

    @property
    def name(self) -> str:
        return self._name

    @name.setter
    def name(self, file_name: str):
        file_format = '.' + file_name.split('.')[-1]
        self._name = str(int(self._created_at.timestamp())).join(choices(string.ascii_lowercase, k=4)) + file_format

    @property
    def _relative_path(self) -> str:
        return self._created_at.date().strftime('%Y/%m/%d')

    @property
    def url(self) -> str:
        nginx_uri: str = cherrypy.config['nginx_uri']
        result = os.path.join(nginx_uri, self._relative_path, self._name)
        return '<a href="{}">{}</a>'.format(result, result)

    def save(self):
        upload_path = Path(cherrypy.config['server_directory']).joinpath(self._relative_path)
        if not os.path.exists(upload_path):
            os.makedirs(upload_path)

        file_path = upload_path.joinpath(self.name)
        file_path.write_bytes(self._data)
