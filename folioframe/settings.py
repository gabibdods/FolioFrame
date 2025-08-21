import os
import sys
from pathlib import Path
from dotenv import load_dotenv

# Version
APP_VERSION = "5.1.8"

# Build absolute paths inside project
BASE_DIR = Path(__file__).resolve().parent.parent

# Load Environment Secrets
env_path = Path(BASE_DIR) / ".env"
load_dotenv(dotenv_path=env_path)

# Secret key
SECRET_KEY = os.getenv("SECRET_KEY")

# Debug
DEBUG = False

# Allowed urls
ALLOWED_HOSTS = [
    "localhost",
    "127.0.0.1",
    "gabrieldigitprint.work",
]

# Installed Apps
INSTALLED_APPS = [
    'bip',
    'foliofin',
    'foliogate',
    'foliohome',
    'rest_framework',
    'django_extensions',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
]

# Middleware Apps
MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'folioframe.middleware.Block',
    'folioframe.middleware.Limit',
    'folioframe.middleware.Authenticate',
    'folioframe.middleware.ErrorRedirect',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

# Urls main library
ROOT_URLCONF = 'folioframe.urls'

# Templates
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / 'templates'],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.request',
                'django.template.context_processors.debug',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

TEMPLATES[0]['OPTIONS']['context_processors'].append('folioframe.context_processors.version')

# WSGI & Gunicorn
WSGI_APPLICATION = 'folioframe.wsgi.application'
SECURE_SSL_REDIRECT = False
SECURE_HSTS_SECONDS = 60
SECURE_HSTS_INCLUDE_SUBDOMAINS = True
SECURE_HSTS_PRELOAD = True
SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')

# HTTPS
SESSION_COOKIE_SECURE = True
CSRF_COOKIE_SECURE = True
SESSION_EXPIRE_AT_BROWSER_CLOSE = True
CSRF_TRUSTED_ORIGINS = [
    "http://localhost",
    "http://127.0.0.1",
    "https://gabrieldigitprint.work",
]
CONN_MAX_AGE = 1

# Database
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': os.getenv("POSTGRES_DB"),
        'USER': os.getenv("POSTGRES_USER"),
        'PASSWORD': os.getenv("POSTGRES_PASSWORD"),
        'HOST': os.getenv("POSTGRES_HOST"),
        'PORT': os.getenv("POSTGRES_PORT"),
    }
}

# Password validation
AUTH_PASSWORD_VALIDATORS = [
    { 'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator', },
    { 'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator', },
    { 'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator', },
    { 'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator', },
]

# Internationalization
LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'UTC'
USE_I18N = True
USE_TZ = True

# HazeGate compatibility configurations
FORCE_SCRIPT_NAME = '/ff'
USE_X_FORWARDED_PORT = True
USE_X_FORWARDED_PREFIX = True

# Static files & Nginx
STATIC_URL = f"{FORCE_SCRIPT_NAME}/static/"
STATIC_ROOT = BASE_DIR / 'staticfiles'
STATICFILES_DIRS = [BASE_DIR / 'static']
USE_X_FORWARDED_HOST = True

# Media
MEDIA_URL = f"{FORCE_SCRIPT_NAME}/media/"
MEDIA_ROOT  = BASE_DIR / 'media'

# Default primary key field type
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

# Contact
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_PORT = 587
EMAIL_USE_TLS = True
EMAIL_HOST_USER = os.getenv("EMAIL_HOST_USER")
EMAIL_HOST_PASSWORD = os.getenv("EMAIL_HOST_PASSWORD")

# Ignore trailing slash in url
APPEND_SLASH = True

# IP Address FastAPI Docker Container Expose
FASTAPI_HOST = os.getenv("FASTAPI_HOST")
FASTAPI_PORT = os.getenv("FASTAPI_PORT")

# Electron Bypass
ELECTRON_BYPASS = os.getenv("ELECTRON_BYPASS")

# Rest Framework
REST_FRAMEWORK = {
    "DEFAULT_AUTHENTICATION_CLASSES": [
        "rest_framework.authentication.SessionAuthentication",
    ],
    "DEFAULT_PERMISSION_CLASSES": [
        "rest_framework.permissions.IsAuthenticated",
    ],
}
