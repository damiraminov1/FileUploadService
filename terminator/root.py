import cherrypy

from terminator.models.file import FileObject


@cherrypy.expose
class Root(object):

    @cherrypy.tools.jinja(template='base.html')
    def index(self):
        return {}

    @cherrypy.expose()
    def upload(self, myFile: cherrypy._cpreqbody.Part):
        file = FileObject(myFile)
        return None
