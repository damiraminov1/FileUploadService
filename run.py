import cherrypy

from terminator.settings import GLOBAL_CONF, APP_CONFIG

cherrypy.config.update(GLOBAL_CONF)

from terminator.root import Root

cherrypy.tree.mount(Root(), '/', APP_CONFIG)

cherrypy.engine.start()
cherrypy.engine.block()
