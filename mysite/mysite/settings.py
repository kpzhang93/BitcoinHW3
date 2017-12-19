"""
Django settings for mysite project.

Generated by 'django-admin startproject' using Django 1.11.7.

For more information on this file, see
https://docs.djangoproject.com/en/1.11/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.11/ref/settings/
"""

import os

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.11/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '2h18*684$xn05ksfy3crgv*lj+hl916e7u!ol!bv*nk@z(a^i&'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ["bithundi.com","www.bithundi.com","localhost"]

# Application definition

INSTALLED_APPS = [
    'user',
    'alert',
    'buyAndSell',
    'Chart',
    'orderBuy',
    'orderSell',
    'orderTrade',
    'tickers',
    'landpage',
    'mainpage',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
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

ROOT_URLCONF = 'mysite.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [
            os.path.join(BASE_DIR, 'user', 'templates'),
            os.path.join(BASE_DIR, 'alert', 'templates'),
            os.path.join(BASE_DIR, 'Chart', 'templates'),
            os.path.join(BASE_DIR, 'buyAndSell', 'templates'),
            os.path.join(BASE_DIR, 'orderBuy', 'templates'),
            os.path.join(BASE_DIR, 'orderSell', 'templates'),
            os.path.join(BASE_DIR, 'orderTrade', 'templates'),
            os.path.join(BASE_DIR, 'tickers', 'templates'),
            os.path.join(BASE_DIR, 'titleCurrencie', 'templates'),
            os.path.join(BASE_DIR, 'landpage', 'templates'),
            os.path.join(BASE_DIR, 'mainpage', 'templates'),
            os.path.join(BASE_DIR, 'mysite', 'templates'),
        ],
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

WSGI_APPLICATION = 'mysite.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.11/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}


# Password validation
# https://docs.djangoproject.com/en/1.11/ref/settings/#auth-password-validators

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


# Internationalization
# https://docs.djangoproject.com/en/1.11/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.11/howto/static-files/

STATIC_ROOT = "/var/www/KapleX/static/"

STATIC_URL = '/static/'

STATICFILES_DIRS = [
    os.path.join(BASE_DIR, 'user', 'static'),
    os.path.join(BASE_DIR, 'landpage', 'static'),
    os.path.join(BASE_DIR, 'mainpage', 'static'),
    os.path.join(BASE_DIR, 'mysite', 'static'),
]
