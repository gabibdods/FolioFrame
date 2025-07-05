from .settings import *

DEBUG = True
ALLOWED_HOSTS = [
    "127.0.0.1",
]
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'dev_db.sqlite3'
    }
}
SECURE_SSL_REDIRECT = False # Trust HTTPS Redirect by Nginx
SECURE_HSTS_SECONDS = 60
SECURE_HSTS_INCLUDE_SUBDOMAINS = False
SECURE_HSTS_PRELOAD = False
SECURE_PROXY_SSL_HEADER = ()
# HTTPS
SESSION_COOKIE_SECURE = False
CSRF_COOKIE_SECURE = False
SESSION_EXPIRE_AT_BROWSER_CLOSE = False
CSRF_TRUSTED_ORIGINS = [
    "http://127.0.0.1:9000",
]
CONN_MAX_AGE = 9999
USE_X_FORWARDED_HOST = False