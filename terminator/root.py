# import files
import random
import string
import cherrypy


# function to read file content
def readf(filename):
    file = open(filename)
    read = file.read()
    return read


@cherrypy.expose
class Root(object):

    @cherrypy.tools.jinja(template='base.html')
    def index(self):
        return {}

    @cherrypy.expose()
    def store(self, myFile):
        f = readf(myFile)  # read the uploaded file
        return f
