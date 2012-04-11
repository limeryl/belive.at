# -*- coding: utf-8 -*-

"""Index page."""

import logging
logger = logging.getLogger(__name__)

from pyramid.security import NO_PERMISSION_REQUIRED as PUBLIC
from pyramid.view import view_config

@view_config(route_name='index', permission=PUBLIC,
        renderer='beliveat:templates/index.mako')
def index_view(request):
    return {'world': 'world'}


