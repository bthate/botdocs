#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from setuptools import setup

def read():
    return open("README.rst", "r").read()

setup(
    name='botdocs',
    version='2',
    url='https://github.com/bthate/botdocs',
    author='Bart Thate',
    author_email='bthate@dds.nl',
    description="documentation for BOTLIB",
    long_description=read(),
    license='Public Domain',
    zip_safe=False,
    install_requires=["botlib"],
    scripts=["bin/botdoc"],
    packages=["botdoc",],
    classifiers=['Development Status :: 3 - Alpha',
                 'License :: Public Domain',
                 'Operating System :: Unix',
                 'Programming Language :: Python',
                 'Topic :: Utilities'
                ]
)
