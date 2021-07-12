import cherrypy
from terminator import settings
from terminator.jinjatool import JinjaTool

cherrypy.tools.jinja = JinjaTool(settings.TEMPLATES_PATH)
