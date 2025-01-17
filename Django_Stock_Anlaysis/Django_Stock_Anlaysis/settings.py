import logging
import os
import environ

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
base = environ.Path(__file__)

env = environ.Env(DEBUG=(bool, False))
environ.Env.read_env()

SECRET_KEY = env('SECRET_KEY')
DEBUG = env("DEBUG")
DB = env.db()
ALLOWED_HOSTS = ['*']




DEFAULT_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
]

PROJECT_APPS = [
    'stocks_detail_api.apps.StocksDetailApiConfig',
    'stocks_detail_fe.apps.StocksDetailFeConfig',
]

THIRD_PARTY_APPS = [
    'rest_framework', # for api plugins
    'drf_yasg', # for swagger plugins
    'django_filters', # for filtering in apis
]

INSTALLED_APPS = DEFAULT_APPS + PROJECT_APPS + THIRD_PARTY_APPS

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'Django_Stock_Anlaysis.urls'

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

REST_FRAMEWORK = {

        'DEFAULT_FILTER_BACKENDS': (
            'django_filters.rest_framework.DjangoFilterBackend',),
}

LOGGING = {
    'version': 1,
    'formatters': {
          'verbose': {
              'format': '{levelname} {asctime} {module} --> {message}',
              'style': '{',
          },
      },
    'handlers': {
        'console': {
            'class': 'logging.StreamHandler',
        },
        'file':{
            'level': 'DEBUG',
            'class': 'logging.handlers.RotatingFileHandler',
            'formatter': 'verbose',
            'maxBytes': 1024*1024*1, # 1MB
            'backupCount': 3,
            'filename': os.path.join(BASE_DIR, 'stocks_detail_api.log'),
        }
    },
    'loggers': {
        'django': {
            'handlers': ['file'],
            'level': logging.INFO
        },
        'django.request': {
            'handlers': ['file'],
            'level': logging.DEBUG
    },
    },
}

WSGI_APPLICATION = 'Django_Stock_Anlaysis.wsgi.application'

DATABASES = {
    'default': DB
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

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


STATIC_URL = '/static/'
