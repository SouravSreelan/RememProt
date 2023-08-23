"""
WSGI config for virhost_lncr project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/3.2/howto/deployment/wsgi/
"""

import os

from django.core.wsgi import get_wsgi_application

# os.environ['R_HOME']='/usr/lib/R'
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'virhost_lncr.settings')

application = get_wsgi_application()
