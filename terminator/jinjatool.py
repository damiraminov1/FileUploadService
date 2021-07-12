import cherrypy
import jinja2


class JinjaTool(cherrypy.Tool):

    def __init__(self, templates_path: str):
        fs_loader = jinja2.FileSystemLoader(templates_path)
        self.env = jinja2.Environment(loader=fs_loader)
        cherrypy.Tool.__init__(self, 'before_handler', self.render)

    def __call__(self, *args, **kwargs):
        def wrap(f):
            f.exposed = True
            return cherrypy.Tool.__call__(self, *args, **kwargs)(f)

        return wrap

    def render(self, template: str):
        renderer = self.env.get_template(template)
        try:
            data = cherrypy.serving.request.handler()
            if template and isinstance(data, dict):
                cherrypy.serving.request.handler = lambda: renderer.render(**data)
            else:
                cherrypy.serving.request.handler = data
        except TypeError:
            return
