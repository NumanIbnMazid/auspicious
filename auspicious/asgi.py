import os
from decouple import config, Csv

from django.core.asgi import get_asgi_application

if config('IS_PRODUCTION', default=False, cast=bool) == True:
    os.environ.setdefault(
        'DJANGO_SETTINGS_MODULE', 'auspicious.settings.production'
    )
else:
    os.environ.setdefault(
        'DJANGO_SETTINGS_MODULE', 'auspicious.settings.development'
    )

application = get_asgi_application()
