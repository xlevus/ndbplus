#!/usr/bin/env python

import os
from setuptools import setup


def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()

setup(
    name='ndbplus',
    version='0.0.1',
    description='Additional functionality for AppEngine\'s NDB library.',
    long_description=read('README.md'),
    author='Chris Targett',
    author_email='chris@xlevus.net',
    url='http://github.com/xlevus/ndbplus',
    packages=['ndbplus'],
    install_requires=['blinker'],
    classifiers=[],
    keywords='appengine ndb',
    license='',
    setup_requires=['pytest-runner'],
    tests_require=['pytest', 'mock', 'pytest-beds'],
)
