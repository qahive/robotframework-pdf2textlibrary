#!/usr/bin/env python

import re
from os.path import abspath, join, dirname
from setuptools import setup


CURDIR = dirname(abspath(__file__))

with open("README.rst", "r", encoding='utf-8') as fh:
    long_description = fh.read()

with open(join(CURDIR, 'src', 'Pdf2TextLibrary', '__init__.py'), encoding='utf-8') as f:
    VERSION = re.search("\n__version__ = '(.*)'", f.read()).group(1)

setup(
    name='robotframework-pdf2textlibrary',
    version=VERSION,
    author="QA Hive Co.,Ltd",
    author_email="support@qahive.com",
    description='Robot Framework PDF Inspect Library',
    long_description=long_description,
    url='https://github.com/qahive/robotframework-pdf2textlibrary',
    license='Apache License 2.0',
    keywords='robotframework read pdf reports',
    platforms='any',
    zip_safe=False,
    classifiers=[
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Topic :: Software Development :: Testing",
        "Framework :: Robot Framework"
    ],
    package_dir={'': 'src'},
    install_requires=['robotframework', 'pdfminer2', 'chardet'],
    packages=['Pdf2TextLibrary'],
)
