import cherrypy
from cherrypy._cpreqbody import Part

from terminator.auth import Authorization
from terminator.ldap import auth_require
from terminator.models.file import FileObject


class Root(object):
    auth = Authorization()

    @cherrypy.tools.jinja(template='auth.html')
    def index(self):
        return {}

    @cherrypy.expose
    @auth_require()
    def upload(self, myFile: Part):
        file = FileObject(myFile.file.read(), myFile.filename)
        file.save()
        return file.url

    @cherrypy.tools.jinja(template='base.html')
    @auth_require()
    def base(self):
        return {}
