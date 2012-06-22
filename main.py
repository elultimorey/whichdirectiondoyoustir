import os,sys
os.environ['DJANGO_SETTINGS_MODULE'] = 'stir.settings'
sys.path.append('/tmp/stir')

# Google App Engine imports.
from google.appengine.ext.webapp import util

# Force Django to reload its settings.
from django.conf import settings
settings._target = None

import django.core.handlers.wsgi


def main():
	# Create a Django application for WSGI.
	application = django.core.handlers.wsgi.WSGIHandler()
	
	# Run the WSGI CGI handler with that application.
	util.run_wsgi_app(application)

if __name__ == '__main__':
	main()
