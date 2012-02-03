# -*- coding: utf-8 -*-
import os
import PyV8

try:
    import simplejson as json
except ImportError:
    import json  # noqa

from django.template import TemplateSyntaxError, TemplateEncodingError
from django.template.loader import get_template
from django.utils.encoding import smart_unicode

from fest.conf import settings


def fest_error(message):
    raise TemplateSyntaxError(message)


class TemplateGlobal(PyV8.JSClass):

    def __init__(self, template):
        self.__tpl = template

    def __getattr__(self, name):
        if name == '__fest_error':
            return fest_error

        name = 'py%s' % name
        return PyV8.JSClass.__getattribute__(self, name)

    @property
    def py__dirname(self):
        return settings.FEST_ROOT

    def py__read_file(self, filename, encoding=None):
        # parts of compiler
        if settings.DEBUG and filename.endswith('.js'):
            return open(filename).read()

        if filename == self.__tpl.name:
            template = self.__tpl
        else:
            filename = os.path.abspath(filename).lstrip('/')
            template = get_template(filename)
        return template.template_string


class Template(object):

    def __init__(self, template_string, origin=None,
                 name='<Unknown Template>'):
        try:
            template_string = smart_unicode(template_string)
        except UnicodeDecodeError:
            raise TemplateEncodingError('Templates can only be constructed'
                                        ' from unicode or UTF-8 strings.')

        self.template_string = template_string
        self.name = name

    @property
    def context(self):
        if not hasattr(self, '_context'):
            self._context = PyV8.JSContext(TemplateGlobal(self))
        return self._context

    def compile(self):
        with self.context as cenv:
            filename = os.path.join(settings.FEST_ROOT, 'compile.js')
            compiler = cenv.eval('%scompile;' % open(filename).read())
            return compiler(self.name)

    def render(self, context):

        with self.context as env:
            if not settings.DEBUG:
                template = self.template_string
            else:
                template = self.compile()

            # maybe i'm just stupid
            template = """(function(json_string, fest_error) {
                    return %s(JSON.parse(json_string), fest_error);
                })""" % template

            func = env.eval(template)
            return func(json.dumps(list(context).pop()), fest_error)
