from auspicious.settings.common import *
from decouple import config, Csv


SECRET_KEY = config('SECRET_KEY')

DEBUG = config('DEBUG', default=False, cast=bool)

ALLOWED_HOSTS = ['*']
# ALLOWED_HOSTS = config('ALLOWED_HOSTS', default=['test.com'])


# Email Configurations
EMAIL_BACKEND = config('EMAIL_BACKEND', default='')
EMAIL_HOST = config('EMAIL_HOST', default='localhost')
EMAIL_PORT = config('EMAIL_PORT', default=25, cast=int)
EMAIL_HOST_PASSWORD = config('EMAIL_HOST_PASSWORD', default='')
EMAIL_HOST_USER = config('EMAIL_HOST_USER', default='')
EMAIL_USE_TLS = config('EMAIL_USE_TLS', default=False, cast=bool)


# Database

if env.str('DATABASE_URL', default=''):
    DATABASES = {
        'default': env.db(),
    }
else:
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.sqlite3',
            'NAME': BASE_DIR / 'db.sqlite3',
        }
    }

# ======= MYSQL =======
# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.mysql',
#         'NAME': config('RDS_DB_NAME'),
#         'USER': config('RDS_USERNAME'),
#         'PASSWORD': config('RDS_PASSWORD'),
#         'HOST': config('RDS_HOSTNAME'),
#         'PORT': config('RDS_PORT'),
#         'OPTIONS': {
#             'charset': 'utf8mb4',
#             'autocommit': True,
#             'use_unicode': True,
#             'init_command': 'SET storage_engine=INNODB,character_set_connection=utf8mb4,collation_connection=utf8mb4_unicode_ci',
#             'init_command': "SET sql_mode='STRICT_TRANS_TABLES'"
#         },
#     }
# }

# ======= POSTGRESQL =======
# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.postgresql',
#         # 'ENGINE': 'django.db.backends.postgresql_psycopg2',
#         'NAME': config('RDS_DB_NAME'),
#         'USER': config('RDS_USERNAME'),
#         'PASSWORD': config('RDS_PASSWORD'),
#         'HOST': config('RDS_HOSTNAME'),
#         'PORT': config('RDS_PORT'),
#         # 'OPTIONS': {
#         #     'charset': 'utf8mb4',
#         #     'autocommit': True,
#         #     'use_unicode': True,
#         #     'init_command': 'SET storage_engine=INNODB,character_set_connection=utf8mb4,collation_connection=utf8mb4_unicode_ci',
#         #     'init_command': "SET sql_mode='STRICT_TRANS_TABLES'"
#         # },
#     }
# }


# Static Configuration
STATIC_URL = '/static/'
MEDIA_URL = '/media/'

STATICFILES_DIRS = [
    os.path.join(os.path.dirname(BASE_DIR), 'static'),
]
STATIC_ROOT = os.path.join('static_cdn', 'static_root')
MEDIA_ROOT = os.path.join('static_cdn', 'media_root')


# ==================== Security Modules ===================

#CORS_REPLACE_HTTPS_REFERER = True
#HOST_SCHEME = "https://"
#SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')
#SECURE_SSL_REDIRECT = True
#SESSION_COOKIE_SECURE = True
#CSRF_COOKIE_SECURE = True
#SECURE_HSTS_INCLUDE_SUBDOMAINS = True
#SECURE_HSTS_SECONDS = 300  # 1000000
#SECURE_FRAME_DENY = True
#ACCOUNT_DEFAULT_HTTP_PROTOCOL = 'https'

