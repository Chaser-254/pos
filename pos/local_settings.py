import os
import dj_database_url

SECRET_KEY = os.getenv("SECRET_KEY", "your-default-secret-key")

DEBUG = os.getenv('DEBUG', 'False') == 'True'



ALLOWED_HOSTS = ['eve-pos-926d4500456b.herokuapp.com', '127.0.0.1', 'localhost']



DATABASES = {
    'default': dj_database_url.config(default=os.getenv("DATABASE_URL"))
}
