# -*- coding: utf-8 -*-
from setuptools import setup


setup(
    name='django_fest',
    version='0.1dev',
    license='MIT',
    packages=['fest', ],
    install_requires=[
        'PyV8==1.0',
    ],
    dependency_links=[
        'svn+http://pyv8.googlecode.com/svn/trunk/@429#egg=PyV8-1.0',
    ]
)
