from .settings import *

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    },
    'data_db': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'motion',
        'HOST': '',
        'USER': '',
        'PASSWORD': ''
    }
}