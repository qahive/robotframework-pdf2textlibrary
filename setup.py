#!/usr/bin/env python

from os.path import join, dirname
import os

script_dir = os.path.dirname(__file__)
rel_path = "./src/Pdf2TextLibrary/version.py"
version = {}
with open(os.path.join(script_dir, rel_path)) as fp:
    exec(fp.read(), version)


from setuptools import setup

CLASSIFIERS = """
Programming Language :: Python
Topic :: Software Development :: Testing
"""[1:-1]

long_description=open(join(dirname(__file__), 'README.md',)).read()

setup(
    name='robotframework-pdf2textlibrary',
    version=version.get("VERSION"),
    description='Robot Framework PDF Inspect Library',
    long_description=long_description,
    author='bloopark systems GmbH & Co. KG',
    author_email='info@bloopark.com',
    url='https://github.com/qahive/robotframework-pdf2textlibrary',
    license='Apache License 2.0',
    keywords='robotframework read pdf reports',
    platforms='any',
    zip_safe=False,
    classifiers=CLASSIFIERS.splitlines(),
    package_dir={'': 'src'},
    install_requires=['robotframework', 'pdfminer2', 'chardet'],
    packages=['Pdf2TextLibrary'],
)
