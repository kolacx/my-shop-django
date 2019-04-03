# DEBUG = False

ALLOWED_HOSTS = ['*']

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'djangodb',
        'USER': 'django-user-db',
        'PASSWORD': 'qwerty1234',
        'HOST': 'localhost',
        'PORT': '',
    }
}