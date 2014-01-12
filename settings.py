import os

DEBUG=False
XSRF_COOKIES=False
COOKIE_SECRET='asdasdasdasdasdasdasd'
LOGIN_URL='/login'

_local_path=os.path.dirname(__file__)
STATIC_PATH = os.path.join(_local_path,'static')
STATIC_URL_PREFIX='/static/'
DATABASE_DSN=''
TEMPLATE_PATH=os.path.join(_local_path,'templates')
MEDIA_PATH=os.path.join(_local_path,'MEDIA')
ARCHIVOS=os.listdir(MEDIA_PATH)
DEBUG=True
try:
	from local_settings import *
except ImportError:
	pass