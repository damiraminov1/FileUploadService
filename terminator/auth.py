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
