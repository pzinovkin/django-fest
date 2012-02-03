# -*- coding: utf-8 -*-
import os

from django.conf import settings


settings.FEST_ROOT = getattr(settings, 'FEST_ROOT',
        os.path.join(os.path.dirname(__file__), 'static', 'js', 'fest'))

settings.FEST_COMPILED_ROOT = getattr(settings, 'FEST_COMPILED_ROOT',
        os.path.join(settings.STATIC_ROOT, 'js', 'compiled'))
