from .settings_common import *


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.2/howto/deployment/checklist/

ALLOWED_HOSTS = []

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure--7bv=5)05s+iz&pfd0x58bw)8!=mx$3&$5=lllzaf_df5$#5s!'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

# Set up Logging
LOGGING = {
    'version': 1,   # const 1
    'disable_existing_loggers': False,

    # Set up Logger
    'loggers': {
        # Using logger  for django
        'django': {
            'handlers': ['console'],
            'level': 'INFO',
        },

        # Using logger for regular_course application
        'regular_course': {
            'handlers': ['console'],
            'level': 'DEBUG',
        },
    },

    # Set up handlers
    'handlers': {
        'console': {
            'level': 'DEBUG',
            'class': 'logging.StreamHandler',
            'formatter': 'dev'
        },
    },

    # Set up formatters
    'formatters': {
        'dev': {
            'format': '\t'.join([
                '%(asctime)s',
                '[%(levelname)s]',
                '%(pathname)s(Line:%(lineno)d)',
                '%(message)s'
            ])
        },
    }
}

EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'
