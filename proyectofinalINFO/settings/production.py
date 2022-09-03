from .base import *
import dj_database_url
import django_heroku

BASE_DIR = os.path.dirname(os.path.dirname(__file__))




DEBUG = False

DEBUG_PROPAGATE_EXEPTIONS = True
ALLOWED_HOSTS = ['127.0.0.1', '.herokuapp.com']
# No subir en true porque puede mostrar la ruta exacta del archivo de configuración

# Database
# https://docs.djangoproject.com/en/4.0/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql__psycopg2',
        'NAME': 'django-pbpostgres',
        'USER': 'name',
        'PASSWORD': '',
        'HOST': 'localhost',
        'PORT': '',
    }
}

db_from_env= dj_database_url.config(conn_max_age=500)
DATABASES['default'].update(db_from_env)
django_heroku.settings(locals())
STATICFILES_STORAGE= 'whitenoise.storage.CompressedManifestStaticFilesStorage'
STATICFILES_STORAGE= 'whitenoise.storage.CompressedStaticFilesStorage'


STATIC_URL = 'https://g5proyecto.herokuapp.com/static/'
MEDIA_URL = 'https://g5proyecto.herokuapp.com/media/'




