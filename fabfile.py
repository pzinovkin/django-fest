# -*- coding: utf-8 -*-
from fabric.api import local


def test():
    local('django-admin.py test --settings=fest.tests.settings')
