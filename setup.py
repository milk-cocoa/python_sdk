#!/usr/bin/env python

from __future__ import print_function
from distutils.core import setup
try:
    from pip.req import parse_requirements
except ImportError:
    print('Install pip in your computer')
    exit(1)

from src.milkcocoa import __version__ as version


def get_packages():
    import os

    req_path = os.path.join(os.path.abspath(os.path.dirname(__file__)), 'requirements.txt')
    if not os.path.isfile(req_path):
        raise OSError('requirements.txt file not found in project directory')

    requirements = parse_requirements(filename=req_path, session=False)
    requirements = [str(requirement.req) for requirement in requirements]

    return requirements


setup(
    name='Milkcocoa-python-sdk',
    version=version,
    packages=get_packages()
)
