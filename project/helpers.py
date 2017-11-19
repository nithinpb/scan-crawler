import pkgutil
import importlib

from flask import Blueprint
from flask.json import JSONEncoder as BaseJSONEncoder
from .settings import JSON_DATETIME_FORMAT

def register_blueprints(app, package_name, package_path):
    """Register all Blueprint instances on the specified Flask application found
in all modules for the specified package.

:param app: the Flask application
:param package_name: the package name
:param package_path: the package path
"""
    rv = []
    for _, name, _ in pkgutil.iter_modules(package_path):
        m = importlib.import_module('%s.%s' % (package_name, name))
        for item in dir(m):
            item = getattr(m, item)
            if isinstance(item, Blueprint):
                app.register_blueprint(item)
            rv.append(item)
    return rv


class JSONEncoder(BaseJSONEncoder):
    """Custom :class:`JSONEncoder` which respects objects that include the
:class:`JsonSerializer` mixin.
"""
    def default(self, obj):
        if obj is None:
            return '{}'
        if hasattr(obj, 'isoformat'):
            return obj.strftime(JSON_DATETIME_FORMAT)
        if hasattr(obj, 'to_json'):
            return obj.to_json()
        return super(JSONEncoder, self).default(obj)
