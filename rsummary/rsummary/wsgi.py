"""
WSGI config for rsummary project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/4.0/howto/deployment/wsgi/
"""
# 웹서버와 python application인 django가 소통하는데 필요한 프로토콜 (WebServer Gateway Inteface, WSGI)
import os

from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'rsummary.settings')

application = get_wsgi_application()
