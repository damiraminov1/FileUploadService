import cherrypy
from cherrypy._cpreqbody import Part
from terminator.models.file import FileObject


@cherrypy.expose
class Root(object):

    @cherrypy.tools.jinja(template='base.html')
    def index(self):
        return {}

    @cherrypy.expose()
    def upload(self, myFile: Part):
        file = FileObject(myFile.file.read(), myFile.filename)
        file.save()
        return file.url
