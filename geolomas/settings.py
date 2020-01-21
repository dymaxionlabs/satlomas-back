"""
Django settings for geolomas project.

Generated by 'django-admin startproject' using Django 2.2.6.

For more information on this file, see
https://docs.djangoproject.com/en/2.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/2.2/ref/settings/
"""

import os
from datetime import date

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/2.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = os.getenv('SECRET_KEY')

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = int(os.getenv('DEBUG', 1)) > 0

def get_allowed_hosts():
    """
    Get allowed hosts from .env file

    If DEBUG = True and ALLOWED_HOSTS is empty or null,
    default to ['.dymaxionlabs.com']

    """
    hosts = [s for s in os.getenv('ALLOWED_HOSTS', '').split(',') if s]
    if not DEBUG and not hosts:
        hosts = ['.dymaxionlabs.com']
    return hosts

ALLOWED_HOSTS = get_allowed_hosts()

WEBCLIENT_URL = os.getenv('WEBCLIENT_URL')


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.sites',
    'django.contrib.staticfiles',
    'rest_framework',
    'rest_framework.authtoken',
    'allauth',
    'allauth.account',
    'allauth.socialaccount',
    'rest_auth',
    'rest_auth.registration',
    'corsheaders',
    'django_rq',
    'measures',
    'files',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'corsheaders.middleware.CorsMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'geolomas.urls'

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

WSGI_APPLICATION = 'geolomas.wsgi.application'

CORS_ORIGIN_WHITELIST = [
    WEBCLIENT_URL,
]

# Database
# https://docs.djangoproject.com/en/2.2/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.contrib.gis.db.backends.postgis',
        'NAME': os.getenv('DB_NAME'),
        'USER': os.getenv('DB_USER'),
        'PASSWORD': os.getenv('DB_PASSWORD'),
        'HOST': os.getenv('DB_HOST'),
        'PORT': os.getenv('DB_PORT'),
    }
}

# Password validation
# https://docs.djangoproject.com/en/2.2/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME':
        'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME':
        'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME':
        'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME':
        'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]

# Internationalization
# https://docs.djangoproject.com/en/2.2/topics/i18n/

LANGUAGE_CODE = os.getenv('LANGUAGE_CODE', 'en-us')

TIME_ZONE = os.getenv('TIME_ZONE', 'UTC')

USE_I18N = True

USE_L10N = True

USE_TZ = True

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/2.2/howto/static-files/

STATIC_URL = '/static/'

SITE_ID = 1

RQ_QUEUES = {
    'default': {
        'URL': os.getenv('RQ_REDIS_URL', 'redis://localhost:6379/0'),
        'DEFAULT_TIMEOUT': os.getenv('RQ_TIMEOUT', 360),
    }
}

RQ_SHOW_ADMIN_LINK = True

SCIHUB_URL = os.getenv('SCIHUB_URL')
SCIHUB_USER = os.getenv('SCIHUB_USER')
SCIHUB_PASS = os.getenv('SCIHUB_PASS')
IMAGES_PATH = os.path.join(BASE_DIR, 'data', 'images', 's2')
IMAGES_PATH_S1 = os.path.join(BASE_DIR, 'data', 'images', 's1', 'raw')
S2M_PATH = os.getenv('S2M_PATH')

#OTB
OTB_BIN_PATH = os.getenv('OTB_BIN_PATH')
GDAL_BIN_PATH = os.getenv('GDAL_BIN_PATH')

#MODIS
MODIS_USER = os.getenv('MODIS_USER')
MODIS_PASS = os.getenv('MODIS_PASS')
MODIS_PLATFORM = os.getenv('MODIS_PLATFORM', 'MOLA')
MODIS_PRODUCT = os.getenv('MODIS_PRODUCT','MYD13Q1.006')
MODIS_OUT_DIR = os.getenv('MODIS_OUT_DIR')
MODIS_TIF_DIR = os.getenv('MODIS_TIF_DIR')
