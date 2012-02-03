# -*- coding: utf-8 -*-
import os

PROJECT_ROOT = os.path.dirname(__file__)

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': ':memory:',
    }
}

STATIC_ROOT = os.path.join(PROJECT_ROOT, 'static')

TEST_RUNNER = 'django_nose.NoseTestSuiteRunner'

INSTALLED_APPS = (
    'django_nose',
)

TEMPLATE_LOADERS = (
    'fest.loaders.FSLoader',
    'fest.loaders.AppLoader',
)

TEMPLATE_DIRS = (
    os.path.join(PROJECT_ROOT, 'templates'),
)

STATIC_ROOT = os.path.join(PROJECT_ROOT, 'static')

FEST_ROOT = os.path.join(PROJECT_ROOT, '..', 'static', 'js', 'fest')
FEST_COMPILED_ROOT = os.path.join(STATIC_ROOT, 'js', 'compiled')
