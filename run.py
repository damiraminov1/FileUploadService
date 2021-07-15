import cherrypy

from terminator.root import Root
from terminator.settings import GLOBAL_CONF, APP_CONFIG


cherrypy.config.update(GLOBAL_CONF)

cherrypy.tree.mount(Root(), '/', APP_CONFIG)

cherrypy.engine.start()
cherrypy.engine.block()
