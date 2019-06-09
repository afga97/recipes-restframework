import datetime

from django.conf import settings
# from rest_framework.settings import APISettings

SETTINGS = {}

USER_SETTINGS = getattr(settings, 'JWT_VIEWS_AUTH', {})

DEFAULTS = {
    'JWT_PRIVATE_KEY':
     None,
    'JWT_PUBLIC_KEY':
     None,
    'JWT_SECRET_KEY': settings.SECRET_KEY,
    'JWT_GET_USER_SECRET_KEY': None,
    'JWT_ALGORITHM': 'HS256',
    'JWT_VERIFY': True,
    'JWT_VERIFY_EXPIRATION': True,
    'JWT_LEEWAY': 0,
    'JWT_EXPIRATION_DELTA': datetime.timedelta(seconds=7200),
    'JWT_AUDIENCE': None,
    'JWT_ISSUER': None,

    'JWT_ALLOW_REFRESH': False,
    'JWT_REFRESH_EXPIRATION_DELTA': datetime.timedelta(days=7),

    'JWT_AUTH_HEADER_PREFIX': 'key',
    'JWT_AUTH_COOKIE': None,
}


SETTINGS.update(DEFAULTS)
SETTINGS.update(USER_SETTINGS)