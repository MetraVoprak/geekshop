import json
import os
from pathlib import Path

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = (
    "django-insecure-$5rw9di_jqhuscpkyxi4^zsou&-r=nu=!5v+_ik0arwgo$az3#"
)

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False if os.getenv("DJANGO_PRODUCTION", default=None) else True

ALLOWED_HOSTS = ["*"]


# Application definition

INSTALLED_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    "mainapp",
    "authnapp",
    "basketapp",
    "adminapp",
    "social_django",
    "ordersapp",
]

# Auth model
AUTH_USER_MODEL = "authnapp.ShopUser"

MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    # "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
    "social_django.middleware.SocialAuthExceptionMiddleware",
]

ROOT_URLCONF = "geekshop.urls"

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
                "mainapp.context_processors.basket",
                "social_django.context_processors.backends",
                "social_django.context_processors.login_redirect",
                "django.template.context_processors.media",
            ],
        },
    },
]

WSGI_APPLICATION = "geekshop.wsgi.application"


# Database
# https://docs.djangoproject.com/en/3.2/ref/settings/#databases

if DEBUG:
    DATABASES = {
        "default": {
            "ENGINE": "django.db.backends.sqlite3",
            "NAME": os.path.join(BASE_DIR, "db.sqlite3"),
        }
    }
else:
    DATABASES = {
        "default": {
            "NAME": "geekshop",
            "ENGINE": "django.db.backends.postgresql",
            "USER": "django",
            "PASSWORD": "geekbrains",
            "HOST": "localhost",
        }
    }


# Password validation
# https://docs.djangoproject.com/en/3.2/ref/settings/#auth-password-validators

if not DEBUG:
    AUTH_PASSWORD_VALIDATORS = [
        {
            "NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator",
        },
        {
            "NAME": "django.contrib.auth.password_validation.MinimumLengthValidator",
        },
        {
            "NAME": "django.contrib.auth.password_validation.CommonPasswordValidator",
        },
        {
            "NAME": "django.contrib.auth.password_validation.NumericPasswordValidator",
        },
    ]
else:
    # Set simple password for debug
    AUTH_PASSWORD_VALIDATORS = []


# Internationalization
# https://docs.djangoproject.com/en/3.2/topics/i18n/

LANGUAGE_CODE = "en-us"

TIME_ZONE = "UTC"

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.2/howto/static-files/

STATIC_URL = "/static/"

# In common case STATIC_ROOT can not be in STATICFILES_DIRS
if DEBUG:
    STATICFILES_DIRS = (os.path.join(BASE_DIR, "static"),)
else:
    STATIC_ROOT = os.path.join(BASE_DIR, "static")

# Media files
MEDIA_URL = "/media/"

MEDIA_ROOT = os.path.join(BASE_DIR, "media")

# Set login path:
#   https://docs.djangoproject.com/en/3.2/ref/settings/#login-url
LOGIN_URL = "authnapp:login"

DOMAIN_NAME = "http://localhost:8000"

# Read about sending email:
#   https://docs.djangoproject.com/en/2.2/topics/email/

# Full list of email settings:
#   https://docs.djangoproject.com/en/2.2/ref/settings/#email
EMAIL_HOST = "localhost"
EMAIL_PORT = "25"

EMAIL_USE_SSL = False
# If server support TLS:
# EMAIL_USE_TLS = True

# EMAIL_HOST_USER = "django@geekshop.local"
# EMAIL_HOST_PASSWORD = "geekshop"
# For debugging: python -m smtpd -n -c DebuggingServer localhost:25
EMAIL_HOST_USER = None
EMAIL_HOST_PASSWORD = None

# Email as files
EMAIL_BACKEND = "django.core.mail.backends.filebased.EmailBackend"
EMAIL_FILE_PATH = "tmp/email-messages/"

AUTHENTICATION_BACKENDS = (
    "django.contrib.auth.backends.ModelBackend",
    "social_core.backends.github.GithubOAuth2",
)


with open(
    os.path.join(BASE_DIR, "tmp", "secrets", "github.json"), "r"
) as secrets:
    github_auth = json.load(secrets)

SOCIAL_AUTH_GITHUB_KEY = github_auth["client_id"]
SOCIAL_AUTH_GITHUB_SECRET = github_auth["client_secret"]

# Django Debug Toolbar --->
# if DEBUG:
#     INSTALLED_APPS.extend(
#         [
#             "debug_toolbar",
#             "template_profiler_panel",
#             "django_extensions",
#         ]
#     )


# if DEBUG:
#     MIDDLEWARE.extend(
#         [
#             "debug_toolbar.middleware.DebugToolbarMiddleware",
#         ]
#     )

# # Debgu tool bar settings
# if DEBUG:

#     def show_toolbar(request):
#         return True

#     DEBUG_TOOLBAR_CONFIG = {
#         "SHOW_TOOLBAR_CALLBACK": show_toolbar,
#     }

#     DEBUG_TOOLBAR_PANELS = [
#         # "ddt_request_history.panels.request_history.RequestHistoryPanel",
#         "debug_toolbar.panels.versions.VersionsPanel",
#         "debug_toolbar.panels.timer.TimerPanel",
#         "debug_toolbar.panels.settings.SettingsPanel",
#         "debug_toolbar.panels.headers.HeadersPanel",
#         "debug_toolbar.panels.request.RequestPanel",
#         "debug_toolbar.panels.sql.SQLPanel",
#         "debug_toolbar.panels.templates.TemplatesPanel",
#         "debug_toolbar.panels.staticfiles.StaticFilesPanel",
#         "debug_toolbar.panels.cache.CachePanel",
#         "debug_toolbar.panels.signals.SignalsPanel",
#         "debug_toolbar.panels.logging.LoggingPanel",
#         "debug_toolbar.panels.redirects.RedirectsPanel",
#         "debug_toolbar.panels.profiling.ProfilingPanel",
#         "template_profiler_panel.panels.template.TemplateProfilerPanel",
#     ]
# <--- Django Debug Toolbar

CACHE_MIDDLEWARE_ALIAS = "default"
CACHE_MIDDLEWARE_SECONDS = 120
CACHE_MIDDLEWARE_KEY_PREFIX = "geekbrains"

# Be carefull if you have Windows! Install Memcached before run project!
#     https://www.ubergizmo.com/how-to/install-memcached-windows/
CACHES = {
    "default": {
        "BACKEND": "django.core.cache.backends.memcached.MemcachedCache",
        "LOCATION": "127.0.0.1:11211",
    }
}

LOW_CACHE = True
