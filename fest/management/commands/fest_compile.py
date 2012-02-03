# -*- coding: utf-8 -*-
import os
from fnmatch import fnmatch

from django.conf import settings
from django.core.management.base import NoArgsCommand
from django.core.files.base import ContentFile
from django.core.files.storage import FileSystemStorage
from django.template import TemplateDoesNotExist
from django.template.loader import find_template
from django.template.loaders.cached import Loader as CachedLoader


from fest.template import Template


class Command(NoArgsCommand):

    def handle_noargs(self, **options):
        # Force django to calculate template_source_loaders
        try:
            find_template('notexists')
        except TemplateDoesNotExist:
            pass

        from django.template.loader import template_source_loaders

        loaders = []
        for loader in template_source_loaders:
            if isinstance(loader, CachedLoader):
                loaders.extend(loader.loaders)
            else:
                loaders.append(loader)

        paths = set()
        for loader in loaders:
            paths.update(list(loader.get_template_sources('')))

        templates = set()
        for path in paths:
            for root, dirs, files in os.walk(path):
                templates.update(os.path.join(root, name)
                    for name in files if not name.startswith('.') and
                        fnmatch(name, '*xml'))

        storage = FileSystemStorage(settings.FEST_COMPILED_ROOT)
        for template_name in templates:
            template_file = open(template_name)
            try:
                tpl = Template(template_file.read().decode(
                               settings.FILE_CHARSET))
                template = ContentFile(tpl.compile())
            finally:
                template_file.close()
            name = self.get_dest_filename(template_name)
            storage.delete(name)
            storage.save(name, template)

    def get_dest_filename(self, path):
        path = '%sjs' % path.rstrip('xml')
        parts = path.split(os.sep)[-2:]
        return os.path.join(*parts)
