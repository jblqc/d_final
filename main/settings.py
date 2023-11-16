"""
Django settings for capstone project.

Generated by 'django-admin startproject' using Django 4.2.4.

For more information on this file, see
https://docs.djangoproject.com/en/4.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/4.2/ref/settings/
"""

from pathlib import Path

import os
import sib_api_v3_sdk


# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = "django-insecure-(4mldwfrd@+4hs(hw2h#g!l*fj()if&7qsu3v__dz0rwaakx=q"

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['*']


# Application definition

INSTALLED_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    'whitenoise.runserver_nostatic',    


    # my apps
    "home",
    "charts",
    "chartjs",

    "supermarket",
    "auth_system",
]

MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
    "whitenoise.middleware.WhiteNoiseMiddleware", # <-- add this line

]

ROOT_URLCONF = "main.urls"

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [
            os.path.join(BASE_DIR, 'templates'),
            os.path.join(BASE_DIR, 'template')
        ],

        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                'home.context_processors.context_processors.category_counts',  # Full path to the context processor
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
            ],
        },
    },
]

WSGI_APPLICATION = "main.wsgi.application"


# Database
# https://docs.djangoproject.com/en/4.2/ref/settings/#databases

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": BASE_DIR / "db.sqlite3",
    }
}


# Password validation
# https://docs.djangoproject.com/en/4.2/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/4.2/topics/i18n/

LANGUAGE_CODE = "en-us"

TIME_ZONE = "UTC"

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.2/howto/static-files/

STATIC_URL = 'static/'
STATIC_ROOT = 'staticfiles'
STATICFILES_STORAGE = "whitenoise.storage.CompressedManifestStaticFilesStorage"

# Default primary key field type
# https://docs.djangoproject.com/en/4.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"

LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'handlers': {
        'console': {
            'level': 'DEBUG',
            'class': 'logging.StreamHandler',
        },
    },
    'root': {
        'handlers': ['console'],
        'level': 'DEBUG',
    },
}


# Email Configuration
# EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
# EMAIL_HOST = 'smtp.mailgun.org'  # Replace with your SMTP server's hostname
# EMAIL_PORT = 587  # Port for TLS
# EMAIL_USE_TLS = True  # Use TLS for secure connection
# EMAIL_HOST_USER = 'chichihaku365@gmail.com'
# EMAIL_HOST_PASSWORD = 'HoshiMingyuBoo17'

# # Chichihaku account
# MAILGUN_DOMAIN = 'sandboxf33b5d3d186b4809b9ff609fe14cb829.mailgun.org'
# MAILGUN_API_KEY = '59ad6b2d16b0366a50a0cd0fbccdd850-3750a53b-b670ef50'

EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'in-v3.mailjet.com'  # Replace with your Mailjet SMTP server's hostname
EMAIL_PORT = 587  # Port for TLS
EMAIL_USE_TLS = True  # Use TLS for secure connection


BREVO_API_KEY = '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'

# Update with your sender email address
EMAIL_HOST_USER = 'necessipick@gmail.com'


BASE_URL = 'http://127.0.0.1:8000' # Replace 'index' with the name of your homepage URL


# Email Configuration
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'in-v3.mailjet.com'  # Replace with your Mailjet SMTP server's hostname
EMAIL_PORT = 587  # Port for TLS
EMAIL_USE_TLS = True  # Use TLS for secure connection
# EMAIL_HOST_USER = 'necessipick@gmail.com'  # Your Mailjet API Key
# EMAIL_HOST_PASSWORD = 'ArisPass888@'  # Your Mailjet API Secret

# nece
# MAILJET_API_KEY = '9e243b76f34339282844681dfac16d31'
# MAILJET_API_SECRET = 'a1e594f1c554c219ac4f344ceb6fda27'

# mnl
MAILJET_API_KEY = '657dd9831be5407b26187523ac21afc2'
MAILJET_API_SECRET = '7149d21486c73ca6b7caeddd602673c9'

EMAIL_HOST_USER = 'mnlbaltazar@tip.edu.ph'  # Your Mailjet API Key
# EMAIL_HOST_PASSWORD = 'ArisPass888@'  # Your Mailjet API Secret

# Update with your Brevo API key
BREVO_API_KEY = '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'

# Update with your sender email address
EMAIL_HOST_USER = 'necessipick@gmail.com'


# NecessiPick Account
# MAILGUN_DOMAIN = ''
# MAILGUN_API_KEY = ''

# EMAIL_HOST_USER = 'necessipick@gmail.com'
# EMAIL_HOST_PASSWORD = 'ArisPass888@'

# Add BASE_URL below the email settings
# BASE_URL = reverse_lazy('reset_password_form')  # Replace 'index' with the name of your homepage URL
# BASE_URL = 'http://127.0.0.1:8000/password-reset{token}/' # Replace 'index' with the name of your homepage URL

# BASE_URL = 'http://127.0.0.1:8000/reset_password_form' # Replace 'index' with the name of your homepage URL

# BASE_URL = 'http://127.0.0.1:8000/' # Replace 'index' with the name of your homepage URL

# brevo | nece acc
SMTP_KEY = 'key:xsmtpsib-105615f439a9f9dbf84dac9838ec75bab0545d36acb00a8ee87577a98eba9184-S8RCXyLFGzZgAvwK'
