import ldap
import cherrypy
from typing import Optional


LDAP_DOMAIN = cherrypy.config['ldap_domain']
LDAP_BASE = cherrypy.config['ldap_base']
LDAP_SERVER = cherrypy.config['ldap_server']

_cp_config = {
    'tools.session.on': True,
    'tools.auth.on': True,
}


def auth_require():
    def decorate(f):
        if not hasattr(f, '_cp_config'):
            f._cp_config = dict()
        if 'auth.require' not in f._cp_config:
            f._cp_config['auth.require'] = True
        return f
    return decorate


def check_credentials(username, password):
    # if not username:
    #     return 'Не задан логин.', None
    # if not password:
    #     return 'Не задан пароль.', None
    #
    # ldap_client = ldap.initialize(LDAP_SERVER)
    # ldap_client.set_option(ldap.OPT_REFERRALS, 0)
    # dn = '{}@{}'.format(username, LDAP_DOMAIN)
    # try:
    #     ldap_client.simple_bind_s(dn, password)
    # except ldap.INVALID_CREDENTIALS:
    #     return 'Неправильное имя пользователя или пароль.', None
    return 'Успех!', True


def check_auth(*args, **kwargs):
    # login: Optional[str] = cherrypy.session.get("login")
    login: Optional[str] = cherrypy.session["login"]
    if cherrypy.request.config.get("auth.require"):
        if not login:
            raise cherrypy.HTTPRedirect("/auth")
        cherrypy.request.login = login
    elif login:
        raise cherrypy.HTTPRedirect("/")
