import os
# import dj_database_url

SECRET_KEY = 'django-insecure-504x&av9c7f3w2+ib5u9g2)w7+lwsba#)2%70c*nx(t!y&!e=w'

# SECRET_KEY = os.getenv("SECRET_KEY", "your-default-secret-key")

DEBUG = os.getenv('DEBUG', 'False') == 'True'



ALLOWED_HOSTS = ['eve-pos-926d4500456b.herokuapp.com', '127.0.0.1', 'localhost']


DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'pos',
        'USER': 'postgres',
        'PASSWORD': 'Manu@254#',
        'HOST': '127.0.0.1',
        'PORT': '5432',
    }
}

# DATABASES = {
#     'default': dj_database_url.config(default=os.getenv("DATABASE_URL"))
# }
