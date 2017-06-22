"""
Basic start for running on Bluemix
"""

# Always prefer setuptools over distutils
from setuptools import setup
# To use a consistent encoding
from codecs import open
from os import path

here = path.abspath(path.dirname(__file__))

# Get the long description from the README file
with open(path.join(here, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()

setup(
    name='python-flask-uwsgi',
    version='0.0.1',
    description='Rest API / service flask server by uwsgi',
    long_description=long_description,
    url='https://github.com/...',
    license='...'
)
