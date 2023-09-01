import os
from pathlib import Path

import pymysql  
pymysql.install_as_MySQLdb()


BASE_DIR = Path(__file__).resolve().parent.parent

SECRET_KEY = 'django-insecure-6y_k8_amv&2(r3qhnmy0j7=1l)b9-u3(sb^m0br6ga=6dfcu*6'

DEBUG = True

ALLOWED_HOSTS=['localhost', 'ciods.in']
# ALLOWED_HOSTS=['*']
CSRF_TRUSTED_ORIGINS = ['http://localhost:3000']

INSTALLED_APPS = [
    'whitenoise.runserver_nostatic',
    'accounts.apps.AccountsConfig',
    'rememb_prot.apps.RemembProtConfig',
    'ciods.apps.CiodsConfig',
    'contact.apps.ContactConfig',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'corsheaders'
]


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

ROOT_URLCONF = 'virhost_lncr.urls'


TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / 'templates'],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
            'libraries':{
            'custom_tags': 'virhost_lncr.templatetags.custom_tags',

            }
        },
    },
]

CORS_ORIGIN_WHITELIST = [
    'http://localhost:3000',  # Replace with your Next.js frontend URL
]

CORS_ALLOW_CREDENTIALS = True
CORS_ORIGIN_ALLOW_ALL = False

WSGI_APPLICATION = 'virhost_lncr.wsgi.application'

# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.sqlite3',
#         'NAME': BASE_DIR / 'db.sqlite3',
#     }
# }

# https://stackoverflow.com/questions/29932363/how-to-connect-django-in-ec2-to-a-postgres-database-in-rds

DATABASES = {
'default': {
    'ENGINE': 'django.db.backends.mysql',
    'NAME': 'ciodsdb',
    'USER': 'admin',
    'PASSWORD': 'ciods123',
    'HOST': 'ciodsdb.cubtgfved0u5.us-west-1.rds.amazonaws.com',
    'PORT': '3306',

      'OPTIONS': {
            'autocommit': True,
        },
        'CONN_MAX_AGE': 3600,
        'ATOMIC_REQUESTS': True,
        'connect_args': {
            'pool_size': 10,
        },
    },
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

# LOGGING = {
# 'version': 1,
# 'disable_existing_loggers': False,
# 'handlers': {
#     'file': {
#         'level': 'ERROR',
#         'class': 'logging.FileHandler',
#         'filename': os.path.join(BASE_DIR,'APPNAME.log'),
#     },
# },
# 'loggers': {
#     'django': {
#         'handlers': ['file'],
#         'level': 'ERROR',
#         'propagate': True,
#     },
# },
# }

SESSION_COOKIE_AGE = 1209600 # 15 Minutes

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True

DATA_UPLOAD_MAX_NUMBER_FIELDS = None


STATIC_URL = '/static/'
STATICFILES_LOCATION = 'static'
STATIC_ROOT = os.path.join(BASE_DIR, 'static')


MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media/')


DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
AUTH_USER_MODEL = 'accounts.UserBase'
LOGIN_REDIRECT_URL = '/proteoark/'
LOGIN_URL = '/accounts/login/'

#email setting
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_PORT = '587'
EMAIL_HOST_USER = 'virhostlncrdb@gmail.com'
EMAIL_HOST_PASSWORD = '4vp09is010'
EMAIL_USE_TLS = True


