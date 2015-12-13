#!/usr/bin/env python

from __future__ import print_function
from setuptools import setup
try:
    from pip.req import parse_requirements
except ImportError:
    print('Install pip in your computer')
    exit(1)

from milkcocoa import __version__ as version


def get_packages():
    import os

    req_path = os.path.join(os.path.abspath(os.path.dirname(__file__)), 'requirements.txt')
    if not os.path.isfile(req_path):
        raise OSError(req_path + 'file not found in project directory')

    requirements = parse_requirements(filename=req_path, session=False)
    requirements = [requirement.req.project_name for requirement in requirements]

    return requirements

setup(
    name='milkcocoa-python-sdk',
    version=version,
    install_requires=get_packages(),
    packages=['milkcocoa']
)
