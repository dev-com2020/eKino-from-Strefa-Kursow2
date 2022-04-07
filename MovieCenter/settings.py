import string
import os
from decouple import config

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# ==============================================================================
# CORE SETTINGS
# ==============================================================================

SECRET_KEY = config("SECRET_KEY", default=string.ascii_letters)

DEBUG = config("DEBUG", default=True, cast=bool)
# DEBUG = False
ALLOWED_HOSTS = ['localhost', '127.0.0.1']
DEFAULT_CHARSET = 'utf-8'

INSTALLED_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    "django.contrib.sites",
    # Third-party
    "crispy_forms",
    "debug_toolbar",
    "widget_tweaks",
    'six',

    # Local
    "apps.account",
    "apps.cart",
    "apps.core",
    "apps.checkout",
    "apps.movie",
    "captcha",
]

SITE_ID = 1

INTERNAL_IPS = ["127.0.0.1"]

if config("USE_DOCKER", default=False, cast=bool):
    import socket

    hostname, _, ips = socket.gethostbyname_ex(socket.gethostname())
    INTERNAL_IPS += [ip[:-1] + "1" for ip in ips]

AUTH_USER_MODEL = "account.CustomerUser"

ROOT_URLCONF = "MovieCenter.urls"

WSGI_APPLICATION = "MovieCenter.wsgi.application"

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": os.path.join(BASE_DIR, "db.sqlite3"),
    }
}

# ==============================================================================
# MIDDLEWARE SETTINGS
# ==============================================================================

MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    #"django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
    "debug_toolbar.middleware.DebugToolbarMiddleware",
]

# ==============================================================================
# TEMPLATES SETTINGS
# ==============================================================================

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [os.path.join(BASE_DIR, "apps/templates")],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
            ],
        },
    },
]

# ==============================================================================
# AUTHENTICATION AND AUTHORIZATION SETTINGS
# ==============================================================================

AUTH_PASSWORD_VALIDATORS = [
    {
        "NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator",
    },
    {"NAME": "django.contrib.auth.password_validation.MinimumLengthValidator", },
    {"NAME": "django.contrib.auth.password_validation.CommonPasswordValidator", },
    {"NAME": "django.contrib.auth.password_validation.NumericPasswordValidator", },
]

AUTHENTICATION_BACKENDS = (
    "django.contrib.auth.backends.ModelBackend",
    "allauth.account.auth_backends.AuthenticationBackend",
    'apps.account.authentication.EmailAuthBackend',
)

LOGIN_REDIRECT_URL = "core:home"
LOGOUT_REDIRECT_URL = "login"
LOGIN_URL = "login"
SESSION_REMEMBER = True
ACCOUNT_SIGNUP_PASSWORD_ENTER_TWICE = True
ACCOUNT_USERNAME_REQUIRED = False
ACCOUNT_EMAIL_REQUIRED = True
ACCOUNT_UNIQUE_EMAIL = True

# ==============================================================================
# INTERNATIONALIZATION AND LOCALIZATION SETTINGS
# ==============================================================================

LANGUAGE_CODE = "pl"

TIME_ZONE = "Europe/Warsaw"

USE_I18N = True

USE_L10N = True

USE_TZ = True

# ==============================================================================
# STATIC + MEDIA FILES SETTINGS
# ==============================================================================

STATIC_URL = "/static/"
STATIC_ROOT = os.path.join(BASE_DIR, "static")
STATICFILES_DIRS = [os.path.join(BASE_DIR, "apps/static")]

STATICFILES_FINDERS = [
    "django.contrib.staticfiles.finders.FileSystemFinder",
    "django.contrib.staticfiles.finders.AppDirectoriesFinder",
]

MEDIA_URL = "/media/"
MEDIA_ROOT = os.path.join(BASE_DIR, "media")

# ==============================================================================
# EMAIL SETTINGS
# ==============================================================================

EMAIL_BACKEND = "django.core.mail.backends.smtp.EmailBackend"
EMAIL_FILE_PATH = os.path.join(BASE_DIR, "sent_emails")
EMAIL_HOST = "smtp.gmail.com"
EMAIL_PORT = 587
EMAIL_HOST_USER = "devcomblog@gmail.com"
EMAIL_HOST_PASSWORD = "Devcom123"
EMAIL_USE_TLS = True
DEFAULT_FROM_EMAIL = "MovieCenter <noreply@MovieCenter.com>"

# ==============================================================================
# CACHE SETTINGS
# ==============================================================================

# ==============================================================================
# THIRD-PARTY APPS SETTINGS
# ==============================================================================
CRISPY_TEMPLATE_PACK = "bootstrap4"

# recaptcha v2
RECAPTCHA_PRIVATE_KEY = '6LcS1_QUAAAAAKY8Cb19HUbH0njc12hJ5fkBrDbr'
RECAPTCHA_PUBLIC_KEY = '6LcS1_QUAAAAAKGogcDJIdM2B-kEs1zR8yjj8jNK'

# recaptcha v3
# RECAPTCHA_PRIVATE_KEY = '6LesVPIUAAAAAG6yUCpJKc348za_ItyIq0ElsP1V'
# RECAPTCHA_PUBLIC_KEY = '6LesVPIUAAAAANPzZoKAhDS6KmIFqcgp_M5ruLaN'
# RECAPTCHA_DEFAULT_ACTION = 'generic'
# RECAPTCHA_SCORE_THRESHOLD = 0.5
# ==============================================================================
# SECURITY
# ==============================================================================
SESSION_COOKIE_AGE = 3600  # one hour

# Cross site request forgery (CSRF) protection
SESSION_COOKIE_SECURE = True
CSRF_COOKIE_SECURE = True

# Cross-site Scripting (XSS)
SECURE_BROWSER_XSS_FILTER = True
SECURE_CONTENT_TYPE_NOSNIFF = True

X_FRAME_OPTIONS = 'SAMEORIGIN'
