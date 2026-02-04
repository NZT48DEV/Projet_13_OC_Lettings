from django.core.handlers.asgi import ASGIHandler
from django.core.handlers.wsgi import WSGIHandler

import oc_lettings_site.asgi as asgi_module
import oc_lettings_site.wsgi as wsgi_module


def test_entrypoints_modules():
    assert isinstance(wsgi_module.application, WSGIHandler)
    assert isinstance(asgi_module.application, ASGIHandler)
