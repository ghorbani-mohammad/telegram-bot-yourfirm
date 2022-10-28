import os
import environ
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent

DEBUG = True
env = environ.Env()
environ.Env.read_env(os.path.join(BASE_DIR, '.env'))
SECRET_KEY = 'django-insecure-1nv*-1bq#6=b3j2&$kritu^g)g0_a7zk9h5cy=t-49o-8v&=^w'


ALLOWED_HOSTS = ['.ngrok.io', 'localhost']
CSRF_TRUSTED_ORIGINS = ['http://*.ngrok.io', 'https://*.ngrok.io']


INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'api',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'telegrambot.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'telegrambot.wsgi.application'


DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}


AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]


USE_TZ = True
USE_I18N = True
TIME_ZONE = 'UTC'
LANGUAGE_CODE = 'en-us'


STATIC_URL = 'static/'

# Default primary key field type
# https://docs.djangoproject.com/en/4.0/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

TEST_ACCOUNT_ID = env.int('TEST_ACCOUNT_ID', default=1)
TELEGRAM_AUTH_TOKEN = env('TELEGRAM_AUTH_TOKEN', default='')
TELEGRAM_URL = f'https://api.telegram.org/bot{TELEGRAM_AUTH_TOKEN}/'

REDIS_DB = env('REDIS_DB', default=0)
REDIS_PORT = env('REDIS_PORT', default=6379)
REDIS_HOST = env('REDIS_HOST', default='redis_host')

YOURFIRM_URL = 'https://www.yourfirm.de'
YOURFIRM_RESPONSE_CACHE_TIME = env('YOURFIRM_RESPONSE_CACHE_TIME', default=10 * 60)
