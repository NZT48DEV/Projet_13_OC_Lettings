import logging
import os
from pathlib import Path

import sentry_sdk
from dotenv import load_dotenv
from sentry_sdk.integrations.django import DjangoIntegration
from sentry_sdk.integrations.logging import LoggingIntegration

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = Path(__file__).resolve().parent.parent

try:
    import colorlog  # noqa: F401

    HAS_COLORLOG = True
except Exception:
    HAS_COLORLOG = False

load_dotenv(BASE_DIR / ".env")

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = os.getenv("SECRET_KEY")
if not SECRET_KEY:
    raise RuntimeError("SECRET_KEY is not set in environment")


# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = os.getenv("DEBUG", "False").lower() in ("1", "true", "yes", "on")

ALLOWED_HOSTS = [
    h.strip() for h in os.getenv("ALLOWED_HOSTS", "").split(",") if h.strip()
]


def env_bool(name: str, default: bool = False) -> bool:
    return os.getenv(name, str(default)).strip().lower() in {"1", "true", "yes", "on"}


def env_float(name: str, default: float = 0.0) -> float:
    try:
        return float(os.getenv(name, default))
    except ValueError:
        return default


# Sentry logging level
EVENT_LEVEL = os.getenv("EVENT_LEVEL", "WARNING").upper()

LOG_LEVEL_MAP = {
    "DEBUG": logging.DEBUG,
    "INFO": logging.INFO,
    "WARNING": logging.WARNING,
    "ERROR": logging.ERROR,
    "CRITICAL": logging.CRITICAL,
}

sentry_logging = LoggingIntegration(
    level=None,
    event_level=LOG_LEVEL_MAP.get(EVENT_LEVEL, logging.WARNING),
)

SENTRY_DSN = os.getenv("SENTRY_DSN", "").strip()

# Sentry init
if SENTRY_DSN:
    app_release = os.getenv("SENTRY_RELEASE", "oc-lettings@0.0.0").strip()

    git_sha = (os.getenv("RENDER_GIT_COMMIT") or os.getenv("GIT_SHA") or "").strip()

    release = f"{app_release}+{git_sha[:7]}" if git_sha else app_release

    sentry_sdk.init(
        dsn=SENTRY_DSN,
        integrations=[DjangoIntegration(), sentry_logging],
        environment=os.getenv("SENTRY_ENVIRONMENT", "development"),
        release=release,
        enable_logs=env_bool("SENTRY_ENABLE_LOGS", False),
        attach_stacktrace=env_bool("ATTACH_STACKTRACE", False),
        traces_sample_rate=env_float("SENTRY_TRACES_SAMPLE_RATE", 0.0),
        profiles_sample_rate=env_float("SENTRY_PROFILES_SAMPLE_RATE", 0.0),
        send_default_pii=env_bool("SEND_DEFAULT_PII", False),
    )

# Application definition

INSTALLED_APPS = [
    "oc_lettings_site.apps.OCLettingsSiteConfig",
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    "lettings",
    "profiles",
]

if DEBUG:
    INSTALLED_APPS += ["django_extensions"]

MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "whitenoise.middleware.WhiteNoiseMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
    "oc_lettings_site.middleware.request_logging.RequestLoggingMiddleware",
]

ROOT_URLCONF = "oc_lettings_site.urls"

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [os.path.join(BASE_DIR, "templates")],
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

WSGI_APPLICATION = "oc_lettings_site.wsgi.application"


# Database
# https://docs.djangoproject.com/en/3.0/ref/settings/#databases

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": os.path.join(BASE_DIR, "oc-lettings-site.sqlite3"),
    }
}


# Password validation
# https://docs.djangoproject.com/en/3.0/ref/settings/#auth-password-validators

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


# Internationalization
# https://docs.djangoproject.com/en/3.0/topics/i18n/

LANGUAGE_CODE = "en-us"

TIME_ZONE = "UTC"

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.0/howto/static-files/

STATIC_ROOT = os.path.join(BASE_DIR, "staticfiles")

STATIC_URL = "/static/"
STATICFILES_DIRS = [
    BASE_DIR / "static",
]

LOG_LEVEL = os.getenv("LOG_LEVEL", "INFO").upper()
LOG_FORMAT = (
    "[%(asctime)s.%(msecs)03d]"
    "%(log_color)s %(levelname)s %(reset)s "
    "%(name)s %(message)s"
)

LOG_DIR = BASE_DIR / "logs"
LOG_DIR.mkdir(exist_ok=True)

LOGGING = {
    "version": 1,
    "disable_existing_loggers": False,
    "formatters": {
        "django_server": {
            "format": "[%(asctime)s.%(msecs)03d] %(message)s",
            "datefmt": "%d/%b/%Y %H:%M:%S",
        },
        "console": (
            {
                "()": "colorlog.ColoredFormatter",
                "fmt": LOG_FORMAT,
                "datefmt": "%d/%b/%Y %H:%M:%S",
                "log_colors": {
                    "DEBUG": "cyan",
                    "INFO": "green",
                    "WARNING": "yellow",
                    "ERROR": "red",
                    "CRITICAL": "bold_red",
                },
            }
            if HAS_COLORLOG
            else {
                "format": "[%(asctime)s] %(levelname)s %(name)s %(message)s",
                "datefmt": "%Y-%m-%d %H:%M:%S",
            }
        ),
        "file": {
            "format": "[%(asctime)s] %(levelname)s %(name)s %(message)s",
            "datefmt": "%Y-%m-%d %H:%M:%S",
        },
    },
    "handlers": {
        "console": {
            "class": "logging.StreamHandler",
            "formatter": "console",
        },
        "django_server": {
            "class": "logging.StreamHandler",
            "formatter": "django_server",
        },
        "file": {
            "class": "logging.handlers.TimedRotatingFileHandler",
            "filename": str(LOG_DIR / "django.log"),
            "when": "midnight",
            "backupCount": 14,
            "encoding": "utf-8",
            "formatter": "file",
        },
        "errors_file": {
            "class": "logging.handlers.TimedRotatingFileHandler",
            "filename": str(LOG_DIR / "errors.log"),
            "when": "midnight",
            "backupCount": 30,
            "encoding": "utf-8",
            "formatter": "file",
            "level": "WARNING",
        },
        "access_file": {
            "class": "logging.handlers.TimedRotatingFileHandler",
            "filename": str(LOG_DIR / "access.log"),
            "when": "midnight",
            "backupCount": 14,
            "encoding": "utf-8",
            "formatter": "file",
        },
    },
    "loggers": {
        "django.server": {
            "handlers": ["django_server"],
            "level": "INFO",
            "propagate": False,
        },
        "django.request": {
            "handlers": ["console", "file", "errors_file"],
            "level": "WARNING",
            "propagate": False,
        },
        "oc_lettings.access": {
            "handlers": ["console", "access_file"],
            "level": "INFO",
            "propagate": False,
        },
    },
    "root": {
        "handlers": ["console", "file"],
        "level": LOG_LEVEL,
    },
}
