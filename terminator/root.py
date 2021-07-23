from cherrypy._cpreqbody import Part
from terminator.models.file import FileObject
import cherrypy
from terminator.ldap import check_auth, check_credentials


class Authorization:

    @staticmethod
    def on_login(username: str):
        cherrypy.request.login = username
        cherrypy.session['login'] = username

    @cherrypy.expose()
    def login(self, username: str, password: str):
        if check_credentials(username, password)[1]:
            self.on_login(username)
            raise cherrypy.HTTPRedirect('/base')
        else:
            raise cherrypy.HTTPRedirect('/index')

    @check_auth()
    def logout(self):
        cherrypy.request.login = ''
        cherrypy.session.pop('login', None)


class Root(object):
    auth = Authorization()

    @cherrypy.tools.jinja(template='auth.html')
    def index(self):
        return {}

    @cherrypy.expose
    @check_auth()
    def upload(self, myFile: Part):
        file = FileObject(myFile.file.read(), myFile.filename)
        file.save()
        return file.url

    @cherrypy.tools.jinja(template='base.html')
    @check_auth()
    def base(self, *args, **kwargs):
        return {}
        # if cherrypy.session['login']:
        #     return {}
        # else:
        #     raise cherrypy.HTTPRedirect('/index')

