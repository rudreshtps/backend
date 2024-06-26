import os
from .settings import *
from .settings import BASE_DIR

ALLOWED_HOSTS = [os.environ['WEBSITE_HOSTNAME']]
CSRF_TRUSTED_ORIGINS = ['https://'+ os.environ['WEBSITE_HOSTNAME']   ]
DEBUG=False
SECRET_KEY=os.getenv('DJANGO_SECRET_KEY')  # Required for Django to work properly.

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'corsheaders.middleware.CorsMiddleware',
]

STATICFILES_STORAGE= 'whitenoise.storage.CompressedManifestStaticFilesStorage'
STATIC_ROOT =   os.path.join(BASE_DIR, "staticfiles")

# conn_str = os.environ['AZURE_POSTGRESQL_CONNECTIONSTRING']
# conn_str_params = {pair.split('=')[0]: pair.split('=')[1] for pair in conn_str.split(' ')}

DATABASES   ={
    'default': {
        'ENGINE': 'djongo',
        'NAME': os.environ.get("DB_NAME"),
        'USER': os.environ.get("DB_USER"),
        'PASSWORD': os.environ.get("DB_PASSWORD"),      
        'HOST': os.environ.get("DB_HOST"),                                          
    }
}