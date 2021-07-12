import cherrypy

# from terminator.jinjatool import JinjaTool
from terminator.settings import GLOBAL_CONF, APP_CONFIG
from terminator.root import Root
# from terminator import settings

if __name__ == "__main__":
    cherrypy.config.update(GLOBAL_CONF)
    cherrypy.quickstart(Root(), '/', APP_CONFIG)
