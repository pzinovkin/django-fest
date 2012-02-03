# -*- coding: utf-8 -*-
import os

from django.template.base import TemplateDoesNotExist
from django.template.loaders import app_directories, filesystem

from fest.conf import settings
from fest.template import Template


def load_compiled(filename):
    filepath = os.path.join(settings.FEST_COMPILED_ROOT, filename)
    filepath = '%sjs' % filepath.rstrip('xml')
    try:
        file = open(filepath)
        try:
            return (file.read().decode(settings.FILE_CHARSET), filepath)
        finally:
            file.close()
    except IOError:
        raise TemplateDoesNotExist('Template %s not found.' % filepath)


class AppLoader(app_directories.Loader):
    is_usable = True

    def load_template(self, template_name, template_dirs=None):
        source, origin = self.load_template_source(template_name,
                                                   template_dirs)
        return Template(source, origin, template_name), origin

    def load_template_source(self, template_name, template_dirs=None):
        if not settings.DEBUG:
            return load_compiled(template_name)
        else:
            return super(AppLoader, self).load_template_source(template_name,
                                                              template_dirs)


class FSLoader(filesystem.Loader):
    is_usable = True

    def load_template(self, template_name, template_dirs=None):
        source, origin = self.load_template_source(template_name,
                                                   template_dirs)
        return Template(source, origin, template_name), origin

    def load_template_source(self, template_name, template_dirs=None):
        if not settings.DEBUG:
            return load_compiled(template_name)
        else:
            return super(FSLoader, self).load_template_source(template_name,
                                                              template_dirs)
