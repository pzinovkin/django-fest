# -*- coding: utf-8 -*-
from django.conf import settings
from django.test import TestCase
from django.template import Context
from django.template.loader import get_template


class CompiledTemplateTest(TestCase):

    def test_render(self):
        t = get_template('doctype.xml')
        self.assertEqual(t.render(Context()), '<!DOCTYPE html>')

    def test_render_context(self):
        t = get_template('base.xml')
        c = Context({'name': 'Jack "The Ripper"'})
        self.assertEqual(t.render(c), '<h1>Hello, Jack "The Ripper"</h1>')

    def test_render_include(self):
        t = get_template('include.xml')
        c = Context({'list': [1, 2]})
        self.assertEqual(t.render(c), '12')


class SourceTemplateTest(CompiledTemplateTest):

    @classmethod
    def setUpClass(cls):
        settings.DEBUG = True

    @classmethod
    def tearDownClass(cls):
        settings.DEBUG = False
