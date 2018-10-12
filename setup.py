#!/usr/bin/env python
# coding=utf-8

import os
import sys

try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

if sys.argv[-1] == 'publish':
    os.system('python setup.py sdist upload')
    sys.exit()

requires = []

setup(
    name='httputil',
    author='Jintao Zhang',
    author_email='zhangjintao9020@gmail.com',
    py_modules=['httputil'],
    install_requires=requires,
    license='MIT',
    zip_safe=False,
    platforms='any',
)
