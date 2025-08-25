import djp

SECRET_KEY = "django-insecure-test-key"
DEBUG = True

INSTALLED_APPS = []

MIDDLEWARE = [
    "django.middleware.locale.LocaleMiddleware",
    "django.middleware.gzip.GZipMiddleware",
    "django.middleware.security.SecurityMiddleware",
]

ROOT_URLCONF = "tests.test_project.urls"

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": ":memory:",
    }
}


djp.settings(globals())
