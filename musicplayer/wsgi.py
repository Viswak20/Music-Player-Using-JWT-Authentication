"""
WSGI config for musicplayer project.

It exposes the WSGI callable as a module-level variable named `application`.
"""

import os
from django.core.wsgi import get_wsgi_application

# Set the Django settings module
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'musicplayer.settings')

# WSGI application callable
application = get_wsgi_application()
