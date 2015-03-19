import ckan.plugins as p
import logging
import urlparse
from ckan.plugins import toolkit

NotAuthorized = toolkit.NotAuthorized
get_action  = toolkit.get_action
abort  = toolkit.abort
_  = toolkit._
c = toolkit.c
request = toolkit.request
NotFound = toolkit.ObjectNotFound

log =logging.getLogger(__name__)

class DatamxController(p.toolkit.BaseController):
    def home(self):
        context = {
            'user': c.user or c.author, 'auth_user_obj': c.userobj
        }
        try:
            data_dict = {'resource': c.resource, 'package': c.package, 'parameters': request.params }
            return p.toolkit.render('home/index.html', data_dict)

        except NotFound:
            abort(404, _('Resource not found'))
        except NotAuthorized:
            abort(401, _('Unauthorized to read resource'))
        except:
            abort(500, _('There was an internal error'))
