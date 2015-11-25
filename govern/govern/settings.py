#!/usr/bin/env python
#  coding: utf-8

"""
Django settings for govern project.

Generated by 'django-admin startproject' using Django 1.8.4.

For more information on this file, see
https://docs.djangoproject.com/en/1.8/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.8/ref/settings/
"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os
import sys

reload(sys)
sys.setdefaultencoding('utf-8')

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

MEDIA_ROOT = os.path.join(BASE_DIR, 'media').replace('\\', '/')
MEDIA_URL = '/media/'

STATIC_ROOT = os.path.join(BASE_DIR, 'static').replace('\\', '/')
STATIC_URL = '/static/'

STATICFILES_DIRS = (
    # Put strings here, like "/home/html/static" or "C:/www/django/static".
    # Always use forward slashes, even on Windows.
    # Don't forget to use absolute paths, not relative paths.
)

STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
    'django.contrib.staticfiles.finders.DefaultStorageFinder',
)

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.8/howto/deployment/checklist/

SITE_ID = 1
# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'r$c=k7w2uat-vfk7*m9li-+g34x9yb$&&u&%5g!b)@-zzoo3hl'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True
ALLOWED_HOSTS = []

# ###########
# EMAIL #
# ###########

EMAIL_PORT = '25'
EMAIL_USE_TLS = True
EMAIL_HOST = 'smtp.mxhichina.com'
EMAIL_HOST_USER = 'administrator@ikuanyu.com'
EMAIL_HOST_PASSWORD = 'WDS926haichuantiandiHi157wjg'

# Default email address to use for various automated correspondence from
# the site managers.
DEFAULT_FROM_EMAIL = 'administrator@ikuanyu.com'
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'

# Subject-line prefix for email messages send with django.core.mail.mail_admins
# or ...mail_managers.  Make sure to include the trailing space.
EMAIL_SUBJECT_PREFIX = '[Django] '

ADMINS = MANAGERS = (
    ('wujuguang', 'wujuguang@ikuanyu.com'),)

# Email address that error messages come from.
SERVER_EMAIL = DEFAULT_FROM_EMAIL
ADMIN_HONEYPOT_EMAIL_ADMINS = True

# 发现一个死链接时, 是否发送一封邮件给 MANAGERS
SEND_BROKEN_LINK_EMAILS = True

DEBUG_TOOLBAR_PATCH_SETTINGS = False

# Application definition
INSTALLED_APPS = (
    'django.contrib.sites',
    'django.contrib.admin',
    'django.contrib.admindocs',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    'debug_toolbar',
    'admin_honeypot',
    'gunicorn',
    'roboter',

    # 'xadmin',
    # 'crispy_forms',
    # 'reversion',
)

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'django.middleware.security.SecurityMiddleware',
    'debug_toolbar.middleware.DebugToolbarMiddleware',
)

ROOT_URLCONF = 'govern.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        # 'BACKEND': 'django.template.backends.jinja2.Jinja2',
        'DIRS': [os.path.join(BASE_DIR, "templates")],
        # app_dirs must not be set when loaders is defined.
        # 'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
            'loaders': [
                'django.template.loaders.filesystem.Loader',
                'django.template.loaders.app_directories.Loader',
                'django.template.loaders.eggs.Loader',
            ],
        },
    },
]

WSGI_APPLICATION = 'govern.wsgi.application'

# Database
# https://docs.djangoproject.com/en/1.8/ref/settings/#databases


DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'roboter',
        'USER': 'develop',
        'PASSWORD': 'f0f2927PfEb9b74F9dE8IWB8p',
        'HOST': '123.57.176.248',
        'PORT': '',
    }
}

# Internationalization
# https://docs.djangoproject.com/en/1.8/topics/i18n/

LANGUAGE_CODE = 'zh-hans'
TIME_ZONE = 'Asia/Shanghai'
USE_I18N = True
USE_L10N = True
USE_TZ = True

# django-debug-toolbar
DEBUG_TOOLBAR_PANELS = [
    'debug_toolbar.panels.versions.VersionsPanel',
    'debug_toolbar.panels.timer.TimerPanel',
    'debug_toolbar.panels.settings.SettingsPanel',
    'debug_toolbar.panels.headers.HeadersPanel',
    'debug_toolbar.panels.request.RequestPanel',
    'debug_toolbar.panels.sql.SQLPanel',
    'debug_toolbar.panels.templates.TemplatesPanel',
    'debug_toolbar.panels.staticfiles.StaticFilesPanel',
    'debug_toolbar.panels.cache.CachePanel',
    'debug_toolbar.panels.signals.SignalsPanel',
    'debug_toolbar.panels.logging.LoggingPanel',
    'debug_toolbar.panels.redirects.RedirectsPanel',
    'debug_toolbar.panels.profiling.ProfilingPanel',
]

DEBUG_TOOLBAR_CONFIG = {
    'JQUERY_URL': 'http://code.jquery.com/jquery-2.1.0.min.js',
}
