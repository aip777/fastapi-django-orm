"""
Django 5.1.4 settings
"""

from pathlib import Path
BASE_DIR = Path(__file__).resolve().parent.parent
SECRET_KEY = 'django-insecure-))!byn^hbk1@p%aa($7*5jddsd23q&ilp$$9%d2ikp4!=7t27^)__w)'

INSTALLED_APPS = [
    'fapi',
]

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
