DEBUG = False

ALLOWED_HOSTS = ['.ais.od.ua']

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'db1',
        'USER': 'db_user_django',
        'PASSWORD': 'XPSP@$#$**)*',
        'HOST': 'localhost',
        'PORT': '',
    }
}